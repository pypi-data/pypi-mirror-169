#
#
#  DNS protocol client / server
#
#
import json
import time

from .binary import *
import re
import sys
import socket
import threading
from .util import rprint


class DnsUtils:
    """ functions for DNS process """
    @staticmethod
    def name_to_bytes(name):
        data = Binary()
        arr = name.split(".")
        for word in arr:
            data.write_byte(len(word))
            data.write_string(word, end_zero=False)
        data.write_byte(0)
        return data.get_bytes()

    @staticmethod
    def value_to_bytes(value, encoding='utf-8'):
        """ convert value to bytes """
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        elif isinstance(value, list) and isinstance(value, dict):
            value = json.dumps(value)

        if isinstance(value, str):
            bs = value.encode(encoding)
            return bs
        else:
            raise ValueError("cannot convert type %s to bytes" % repr(type(value)))

    @staticmethod
    def bytes_to_value(data_bytes, encoding='utf-8'):
        # noinspection PyBroadException
        try:
            s = data_bytes.decode(encoding)
            if s.startswith('{') and s.endswith('}'):
                return json.loads(s)
            else:
                return s
        except Exception:
            pass

    @staticmethod
    def ip_str_to_bytes(ip_str):
        """ convert ip string to bytes """
        if DnsUtils.is_ipv4(ip_str):
            data = Binary()
            arr = ip_str.split(".")
            for word in arr:
                # noinspection PyBroadException
                try:
                    b = int(word)
                    data.write_byte(b)
                except Exception:
                    return None
            return data.get_bytes()
        elif ip_str.find(':') >= 0:
            packet1 = Binary()
            packet2 = Binary()
            data = packet1
            arr = ip_str.split(':')
            for word in arr:
                if len(word) == 0:
                    # there is a '::'
                    data = packet2
                    continue
                # noinspection PyBroadException
                try:
                    n = int('0x' + word, 16)
                    data.write_uint16(n)
                except Exception:
                    return None
            # padding missing zeros
            if data == packet2:
                zero_count = 16 - packet1.size - packet2.size
                for i in range(zero_count):
                    packet1.write_byte(0)
                packet1.write_bytes(packet2.get_bytes())
            return packet1.get_bytes()

    @staticmethod
    def shorten_ipv6(ipv6_str):
        # compress 0000
        ipv6 = ipv6_str.replace(':0000', ':0')
        # remove continuous zero
        ipv6 = ipv6.replace(":0:0:0:0:0:0:", "::")
        ipv6 = ipv6.replace(":0:0:0:0:0:", "::")
        ipv6 = ipv6.replace(":0:0:0:0:", "::")
        ipv6 = ipv6.replace(":0:0:0:", "::")
        ipv6 = ipv6.replace(":0:0:", "::")
        # remove leading zero
        ipv6 = ':' + ipv6
        # ipv6 = re.sub(r':([0]*)([1-9a-fA-F])', r':\2', ipv6)
        ipv6 = re.sub(r':(0*)([1-9a-fA-F])', r':\2', ipv6)
        if ipv6.startswith(':'):
            ipv6 = ipv6[1:]
        return ipv6

    @staticmethod
    def bytes_to_ip_str(ip_bytes):
        """ convert bytes to ip string """
        ret = None
        if ip_bytes is not None:
            if len(ip_bytes) == 4:  # ip v4
                ret = ""
                for i in range(4):
                    if i > 0:
                        ret += "."
                    ret += str(int(ip_bytes[i]) & 0xFF)
            elif len(ip_bytes) == 16:  # ip v6
                ret = ""
                for i in range(16):
                    # ret += '  '
                    if i > 0 and i % 2 == 0:
                        ret += ':'
                    s = hex(int(ip_bytes[i])).lstrip('0x')
                    if len(s) == 0:
                        s = '0'
                    if len(s) == 1:
                        s = '0' + s
                    ret += s
        return ret

    @staticmethod
    def is_ipv4(ip):
        """ whether ip string is ip v4 """
        if isinstance(ip, str):
            # noinspection PyBroadException
            try:
                arr = ip.split(".")
                count = 0
                if len(arr) == 4:
                    for number in arr:
                        n = int(number)
                        if n >= 0:
                            count += 1

                    if count == 4:
                        return True
            except Exception:
                pass
        elif isinstance(ip, bytes) and len(ip) == 4:
            return True
        return False

    @staticmethod
    def send_udp(server, port, request_bytes, timeout=500, retry=1, head_bytes=2):
        """
        send UDP to the server, return response bytes.

        :param server:  the server domain name or IP address. if server=0, broadcast UDP
        :param port:    the port (int)
        :param request_bytes: request bytes
        :param timeout: timeout in milliseconds
        :param retry:   retry times
        :param head_bytes:  (optional)count of response bytes that equals to request bytes
        :return: return response bytes if success. return None if failed.
        """
        if hasattr(request_bytes, 'to_bytes'):
            request_bytes = request_bytes.to_bytes()

        while retry > 0:
            retry -= 1
            client_socket = None
            # noinspection PyBroadException
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                client_socket.settimeout(timeout / 1000.0)
                if str(server) == '0' or server == '255.255.255.255' or server == '0.0.0.0':
                    # send broadcast UDP
                    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    client_socket.sendto(request_bytes, ('255.255.255.255', port))
                else:
                    # send to server
                    client_socket.sendto(request_bytes, (server, port))
                response, _ = client_socket.recvfrom(4096)
                if head_bytes:
                    # compare head bytes
                    for i in range(head_bytes):
                        if response[i] != request_bytes[i]:
                            raise ValueError("unexpected header")
                    return response
                else:
                    return response
            except Exception:
                pass
            finally:
                if client_socket:
                    client_socket.close()

        return None


class ErrorCode:
    """ DNS response code """
    NO_ERROR = 0      # no error
    FORMAT_ERR = 1    # DNS Query Format Error
    SERVICE_FAIL = 2  # Server failed to complete the DNS request
    NX_DOMAIN = 3     # Domain name does not exist.
    NOT_IMPLEMENTED = 4  # Function not implemented
    REFUSED = 5       # The server refused to answer for the query


class EnumType:

    @classmethod
    def get_int(cls, s):
        if isinstance(s, str):
            upper_s = s.upper()
            for item in cls.__dict__:
                if upper_s == item:
                    return cls.__dict__[item]
        elif isinstance(s, int):
            return s

        # noinspection PyBroadException
        try:
            if isinstance(s, str) and s.startswith('0x'):
                return int(s, 16)
            else:
                return int(s)
        except Exception:
            return 0

    @classmethod
    def get_name(cls, n):
        if isinstance(n, int):
            for item in cls.__dict__:
                if str(cls.__dict__[item]) == str(n):
                    return item
        return str(n)


class QueryType(EnumType):
    """ DNS query types (integer constants)"""
    A = 1      # a host IPv4 address
    NS = 2     # an authoritative name server
    CNAME = 5  # the canonical name for an alias
    SOA = 6    # marks the start of a zone of authority
    WKS = 11   # a well known service description
    PTR = 12   # a domain name pointer
    HINFO = 13   # host information
    MX = 15      # mail exchange
    TXT = 16     # text strings
    AAAA = 0x1C  # a host IPv6 address

    # Query TYPE values
    AXFR = 252   # A request for a transfer of an entire zone
    MAILB = 253  # A request for mailbox-related records (MB, MG or MR)
    ANY = 255    # A request for all records


class QueryClass(EnumType):
    """ DNS query classes (integer constants) """
    INET = 1     # the Internet
    CS = 2       # the CSNET class (Obsolete)
    CH = 3       # the CHAOS class
    HS = 4       # Hesiod [Dyer 87]
    ANY = 255    # any class


class Header(Structure):
    """
    DNS message header section.

    SEE: https://www.rfc-editor.org/rfc/rfc1035#section-4.1.1
    """
    id = Uint16

    qr = Bit1
    op_code = Bit4
    aa = Bit1
    tc = Bit1
    rd = Bit1
    ra = Bit1
    z = Bit3
    error_code = Bit4

    question_count = Uint16
    answer_count = Uint16
    name_server_count = Uint16
    additional_count = Uint16


class Question(Structure):
    """
    DNS message question section.

    SEE: https://www.rfc-editor.org/rfc/rfc1035#section-4.1.2
    """
    name = DomainName
    type = Uint16
    clazz = Uint16


class ResourceRecord(Structure):
    """
    DNS message resource record.

    The answer, authority, and additional sections all share the same format:
    Resource DnsRecord.

    SEE: https://www.rfc-editor.org/rfc/rfc1035#section-4.1.3
    """
    name = DomainName
    type = Uint16
    clazz = Uint16
    ttl = Uint32
    length = Uint16

    def __init__(self, name_or_message=None, query_type=None, value=None,
                 ttl=600, clazz=None):
        self._rdata = b''
        self._msg = None
        super().__init__()

        if isinstance(name_or_message, Message):
            self._msg = name_or_message
        elif isinstance(name_or_message, str):
            if query_type is not None and value is not None:
                self._create(name_or_message, query_type, value, ttl, clazz)
            else:
                raise ValueError('query type and value must not be None')

    def _create(self, name, query_type, value, ttl, query_class):
        self.name = name
        self.type = query_type
        self.clazz = query_class
        self.ttl = ttl

        if isinstance(value, bytes):
            self._rdata = value
            self.length = len(self._rdata)
            return

        if self.type == QueryType.A:
            self._rdata = DnsUtils.ip_str_to_bytes(value)
        elif self.type == QueryType.AAAA:
            self._rdata = DnsUtils.ip_str_to_bytes(value)
        elif self.type == QueryType.CNAME:
            self._rdata = DnsUtils.name_to_bytes(value)
        elif self.type == QueryType.MX:
            packet = Binary()
            packet.write_uint16(20)  # preference = 20
            packet.write_domain_name(value)
            self._rdata = packet.to_bytes()
        elif self.type == QueryType.NS:
            self._rdata = DnsUtils.name_to_bytes(value)
        elif self.type == QueryType.PTR:
            self._rdata = DnsUtils.name_to_bytes(value)
        elif self.type == QueryType.SOA:
            try:
                packet = Binary()
                packet.write_domain_name(value['mname'])
                packet.write_domain_name(value['rname'])
                packet.write_uint32(value['serial'])
                packet.write_int32(value['refresh'])
                packet.write_int32(value['retry'])
                packet.write_int32(value['expire'])
                packet.write_uint32(value['minimum'])
                self._rdata = packet.to_bytes()
            except Exception:
                raise ValueError('SOA value invalid')
        elif self.type == QueryType.HINFO:
            self._rdata = DnsUtils.name_to_bytes(value)
        else:
            self._rdata = DnsUtils.value_to_bytes(value)
            # raise ValueError("unknown type %s" % self.type)

        self.length = len(self._rdata)

    def read_binary(self, data, offset=None):
        off, data = super(ResourceRecord, self).read_binary(data, offset)
        rdata_offset = data.offset

        if self.type == QueryType.A:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.4.1
            data_bytes = data.read_bytes(self.length)
            if self.length == 4:
                ip = DnsUtils.bytes_to_ip_str(data_bytes)
                self._msg.ip_list.append((self.name, ip))
        elif self.type == QueryType.AAAA:
            data_bytes = data.read_bytes(self.length)
            if self.length == 16:
                ip = DnsUtils.bytes_to_ip_str(data_bytes)
                ip = DnsUtils.shorten_ipv6(ip)
                self._msg.ipv6_list.append((self.name, ip))
        elif self.type == QueryType.CNAME:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.3.1
            cname = data.read_domain_name()
            self._msg.cname_list.append((self.name, cname))
        elif self.type == QueryType.MX:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.3.9
            # preference = data.read_int16()
            _ = data.read_int16()
            exchange = data.read_domain_name()
            self._msg.mx_list.append((self.name, exchange))
        elif self.type == QueryType.NS:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.3.11
            ns_name = data.read_domain_name()
            self._msg.ns_list.append((self.name, ns_name))
        elif self.type == QueryType.PTR:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.3.12
            ptr_name = data.read_domain_name()
            self._msg.cname_list.append((self.name, ptr_name))
        elif self.type == QueryType.SOA:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.3.13
            mname = data.read_domain_name()  # name server for this zone
            rname = data.read_domain_name()  # the mailbox domain
            serial = data.read_uint32()
            refresh = data.read_int32()
            retry = data.read_int32()
            expire = data.read_int32()
            minimum = data.read_uint32()
            soa = {'mname': mname, 'rname': rname, 'serial': serial, 'refresh': refresh,
                   'retry': retry, 'expire': expire, 'minimum': minimum}
            self._msg.soa_list.append((self.name, soa))
        elif self.type == QueryType.HINFO:
            # https://www.rfc-editor.org/rfc/rfc1035#section-3.3.2
            word = data.read_domain_name()
            if data.offset - rdata_offset + self.length > 0:
                # noinspection PyBroadException
                try:
                    self._rdata = data.read_bytes(data.offset - rdata_offset + self.length)
                except Exception:
                    pass
            self._msg.hinfo_list.append((self.name, word))
        else:
            # other query type
            self._rdata = data.read_bytes(self.length)
            val = DnsUtils.bytes_to_value(self._rdata)
            if val:
                self._msg.values.append(val)

        if data.offset < rdata_offset + self.length:
            # unprocessed bytes
            # noinspection PyBroadException
            self._rdata = data.read_bytes(data.offset - rdata_offset + self.length)
        return off + self.length * 8, data

    @property
    def rdata(self):
        return self._rdata

    def write_binary(self, data=None, offset=None):
        self.length = len(self._rdata)
        offset, data = super().write_binary(data, offset)
        data.write_bytes(self._rdata)
        off = data.offset * 8
        return off, data


class Message:
    """
    DNS message.

    SEE:  https://www.rfc-editor.org/rfc/rfc1035#section-4.1
    """
    DEFAULT_TTL = 600  # default TTL in seconds

    def __init__(self, id_or_bytes=None, query_type=None, name=None, clazz=None):
        """
        create message.

        :param id_or_bytes: (optional)transaction id int, or bytes, or query name str
        :param query_type: (optional)query type int
        :param name:       (optional)query name str
        :param clazz:      (optional)query class int
        :return: return message bytes.
        """

        self.header = Header()
        self.questions = []
        self.bytes = bytes()

        # resource datas
        self.ip_list = []
        self.ipv6_list = []
        self.cname_list = []
        self.ns_list = []
        self.mx_list = []
        self.soa_list = []
        self.hinfo_list = []
        self.values = []

        # response rr
        self._answer_rrs = []
        self._name_server_rrs = []
        self._additional_rrs = []

        if isinstance(id_or_bytes, int) and name:
            # create a query message whose id is specified.
            self.create_query(id_or_bytes, query_type, name, clazz)
        elif isinstance(id_or_bytes, bytes):
            # read message from bytes
            self.from_bytes(id_or_bytes, query_type)
        elif isinstance(id_or_bytes, str):
            # create q query message
            name = id_or_bytes
            id_or_bytes = random.randint(1, 0x7FFF)  # random id
            if query_type is None:
                query_type = QueryType.ANY
            self.create_query(id_or_bytes, query_type, name, clazz)

    def create_query(self, xid, query_type, name, clazz):
        """
        create query message.

        :param xid:   transaction id int
        :param query_type: query type int
        :param name:       query name str
        :param clazz:      query class int
        :return: return message bytes.
        """
        self.header = Header()
        self.header.id = xid
        self.header.rd = 1
        self.header.question_count = 1

        question = Question()
        self.questions.append(question)
        question.name = name
        if isinstance(query_type, str):
            query_type = QueryType.get_int(query_type)
        question.type = query_type if isinstance(query_type, int) else QueryType.A
        question.clazz = clazz if isinstance(clazz, int) else QueryClass.INET

        data = Binary()
        offset, data = self.header.write_binary(data)
        offset, data = question.write_binary(data, offset)
        self.bytes = data.to_bytes()

    def from_bytes(self, data_bytes, length=None):
        """ load message from bytes """
        data = Binary(data_bytes, length=length)
        self.header.read_binary(data, 0)

        # read questions
        # noinspection PyTypeChecker
        for i in range(self.header.question_count):
            question = Question()
            self.questions.append(question)
            question.read_binary(data)

        # read answers
        # noinspection PyTypeChecker
        for i in range(self.header.answer_count):
            ResourceRecord(self).read_binary(data)

        # read name servers
        # noinspection PyTypeChecker
        for i in range(self.header.name_server_count):
            ResourceRecord(self).read_binary(data)

        # read additional
        # noinspection PyTypeChecker
        for i in range(self.header.additional_count):
            ResourceRecord(self).read_binary(data)

    def to_bytes(self):
        """ convert message to bytes """
        return self.bytes

    def to_hex(self, sep='', column=None, prefix=False):
        """
        convert to hex string

        :param sep:     (optional) separator chars
        :param column:  (optional) how many column per row
        :param prefix:  (optional) whether has prefix '0x'
        :return: return hex string
        """
        return Binary(self.bytes).to_hex(sep=sep, column=column, prefix=prefix)

    def __str__(self):
        ret = []
        ret += ["A " + i[0] + " " + str(i[1]) for i in self.ip_list]
        ret += ["AAAA " + i[0] + " " + str(i[1]) for i in self.ipv6_list]
        ret += ["CNAME " + i[0] + " " + str(i[1]) for i in self.cname_list]
        ret += ["NS " + i[0] + " " + str(i[1]) for i in self.ns_list]
        ret += ["MX " + i[0] + " " + str(i[1]) for i in self.mx_list]
        ret += ["SOA " + i[0] + " " + str(i[1]) for i in self.soa_list]
        ret += ["HINFO " + i[0] + " " + str(i[1]) for i in self.hinfo_list]
        ret += ["VALUE " + type(i).__name__ + " " + str(i) for i in self.values]
        return '\n'.join(ret)

    def add_response(self, name, query_type, value, ttl,
                     clazz=QueryClass.INET):
        r = ResourceRecord(name, query_type, value, ttl, clazz)
        if query_type in [QueryType.A, QueryType.AAAA, QueryType.CNAME,
                          QueryType.MX, QueryType.PTR]:
            self._answer_rrs.append(r)
        elif query_type == QueryType.NS:
            self._name_server_rrs.append(r)
        else:
            self._additional_rrs.append(r)

    def response(self, name=None, query_type=None, value=None, ttl=600,
                 query_class=QueryClass.INET):
        if name and query_type is not None and value is not None:
            self.add_response(name, query_type, value, ttl, query_class)

        self.header.qr = 1
        self.header.aa = 1
        self.header.error_code = 0

        self.header.question_count = len(self.questions)
        self.header.answer_count = len(self._answer_rrs)
        self.header.name_server_count = len(self._name_server_rrs)
        self.header.additional_count = len(self._additional_rrs)

        data = Binary()
        self.header.write_binary(data)

        for question in self.questions:
            question.write_binary(data)

        for r in self._answer_rrs:
            r.write_binary(data)
        for r in self._name_server_rrs:
            r.write_binary(data)
        for r in self._additional_rrs:
            r.write_binary(data)

        return data.to_bytes()

    def response_error(self, err_code):
        self.header.qr = 1
        self.header.error_code = err_code
        self.header.answer_count = 0

        data = Binary()
        self.header.write_binary(data)
        question = self.questions[0] if len(self.questions) > 0 else None
        if question:
            question.write_binary(data)
        return data.to_bytes()


class DnsClient:
    """
    DNS client
    """

    def __init__(self, ns_server, port=53):
        self.ns_server = ns_server
        self.port = port
        self.timeout = 500
        self.retry = 2
        self.transaction_id = 0

    def query(self, query_type, query_name, query_class=QueryClass.INET):
        """
        make a query

        :param query_type:  query_type string or int
        :param query_name:  name string
        :param query_class:  (optional)query class
        :return: return Message object if success. return None if failed.
        """
        if isinstance(query_type, str):
            query_type = QueryType.get_int(query_type)

        if not isinstance(query_type, int) or query_type <= 0:
            raise ValueError("query type invalid")

        # noinspection PyBroadException
        try:
            self.transaction_id += 1
            msg = Message(self.transaction_id, query_type, query_name, query_class)

            response_bytes = DnsUtils.send_udp(
                self.ns_server, self.port, msg.to_bytes(), self.timeout, self.retry)

            if response_bytes is not None:
                msg = Message(response_bytes)
                return msg

        except Exception:
            pass

        return None

    def get_ip(self, domain_name):
        """
        get IPv4 address of specified domain name

        :param domain_name:  domain name string
        :return: return IPv4 string if success. return None if failed.
        """
        msg = self.query(QueryType.A, domain_name)
        if msg and len(msg.ip_list) > 0:
            item = msg.ip_list[0]
            return item[1]

    def create_domain(self, domain_name, ip, ttl=600):
        """
        create domain name to specified IP address

        :param domain_name:  domain name string
        :param ip:           IP address string
        :param ttl:          (optional)time to live in seconds
        :return: return IPv4 string if success. return None if failed.
        """
        return self.get_ip(domain_name + "=" + ip + "=" + str(ttl))


class DnsRecord:
    """ A DNS record"""
    def __init__(self, query_type, name, value, ttl, clazz):
        self.type = query_type
        self.name = name
        self.value = value
        self.ttl = ttl
        self.clazz = clazz


class DnsRecords:
    def __init__(self):
        self.store = {}

    # noinspection PyMethodMayBeStatic
    def _query_type_int(self, query_type):
        """ return query type int """
        if not isinstance(query_type, int):
            query_type = QueryType.get_int(str(query_type).upper())
        return query_type

    # noinspection PyMethodMayBeStatic
    def _clazz_int(self, clazz):
        """ return query type int """
        if not isinstance(clazz, int):
            clazz = QueryClass.get_int(str(clazz).upper())
        return clazz

    def add(self, query_type, name, value, ttl=Message.DEFAULT_TTL, clazz=1):
        """
        add a record.

        :param query_type: query type int
        :param name:       name str
        :param value:      value
        :param ttl:        ttl int (seconds)
        :param clazz:      query class int
        :return: self
        """
        query_type = self._query_type_int(query_type)
        clazz = self._clazz_int(clazz)
        r = DnsRecord(query_type, name, value, ttl, clazz)
        catalog = query_type * 1000 + clazz
        if catalog not in self.store:
            self.store[catalog] = {}
        self.store[catalog][name] = r
        return self

    def find(self, query_type, name, clazz, client_ip=None):
        """
         find a record.

        :param query_type: query type int
        :param name:       name str
        :param clazz:      query class int
        :param client_ip:  (optional)client IP address str
        :return: return Record object if success. return None if failed.
        """
        query_type = self._query_type_int(query_type)
        clazz = self._clazz_int(clazz)
        catalog = query_type * 1000 + clazz
        if catalog in self.store:
            return self.store[catalog].get(name, None)

    def remove(self, query_type, name, clazz):
        """ remove record """
        query_type = self._query_type_int(query_type)
        catalog = query_type * 1000 + clazz
        if catalog in self.store:
            if name in self.store[catalog]:
                self.store[catalog].pop(name)

    def save_to_file(self, filename):
        """ save records to file """
        f = open(filename, 'w+')
        for catalog in self.store:
            d = self.store[catalog]
            for key in d:
                record = d[key]
                line = QueryType.get_name(record.type) + ' ' + record.name + ' '\
                       + str(record.ttl) + ' ' + QueryClass.get_name(record.clazz) + ' '\
                       + record.value
                f.write(line + '\n')
        f.close()

    def load_from_file(self, filename):
        """ load records from file """
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.lstrip()
            if line == '' or line.startswith('#'):
                continue
            words = line.split(' ')
            # noinspection PyBroadException
            try:
                query_type = QueryType.get_int(words[0])
                name = words[1]
                ttl = int(words[2])
                clazz = QueryClass.get_int(words[3])
                value = ' '.join(words[4:])
                self.add(query_type, name, value, ttl, clazz)
            except Exception:
                print('ERROR LINE: ' + line)


class DnsServer:
    """
    DNS Server
    """
    def __init__(self, port=53, ip=None):
        self.ip = ip if ip is not None else ''
        self.port = port
        self.upper_dns_server = None
        self.canceled = True
        self.server_socket = None
        self.records = DnsRecords()
        self.is_thread = False

    def __del__(self):
        print("del")
        self.stop()
        time.sleep(0.5)

    def set_upper_dns(self, upper_dns_server):
        """ set upper dns server """
        self.upper_dns_server = upper_dns_server
        return self

    def _find_cache(self, msg: Message, client_address):
        """ find answer in records, return response bytes """
        print(type(client_address), client_address)
        question = msg.questions[0] if len(msg.questions) > 0 else None
        if question:
            if question.name.find("=") > 0:
                return self._create_domain(msg)

            r = self.records.find(question.type, question.name,
                                  question.clazz, client_address[0])
            if isinstance(r, DnsRecord):
                return msg.response(r.name, r.type, r.value, r.ttl, r.clazz)
        return None

    def _create_domain(self, msg: Message):
        """ create domain, return response bytes """
        def split_name(s):
            arr = s.split("=")
            if len(arr) >= 2:
                s_name = arr[0]
                s_ip = arr[1]
                n_ttl = 600
                if len(arr) > 2:
                    # noinspection PyBroadException
                    try:
                        n_ttl = int(arr[2])
                    except Exception:
                        pass
                return s_name, s_ip, n_ttl
            return None, None, None

        question = msg.questions[0] if len(msg.questions) > 0 else None
        if question:
            name, ip, ttl = split_name(question.name)
            if name and ip:
                self.records.add(question.type, name, ip, ttl, question.clazz)
                return msg.response(name, question.type, ip, ttl)
            return msg.response_error(ErrorCode.REFUSED)
        return None

    def _run(self, prompt=None):
        """ run the server """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.ip, self.port))

        if prompt is True:
            rprint('DNS server started at port', self.port)
        elif isinstance(prompt, str):
            rprint(prompt)

        self.canceled = False
        while not self.canceled:
            # noinspection PyBroadException
            try:
                # if self.is_thread is True:
                #     self.server_socket.settimeout(2)
                request, client_address = self.server_socket.recvfrom(2048)
                msg = Message(request)
                response_bytes = self._find_cache(msg, client_address)
                if response_bytes:
                    self._send_response(client_address, response_bytes)
                elif self.upper_dns_server:
                    self._query_upper_dns(client_address, request)
                else:
                    self._send_error_response(client_address, request)
            except socket.timeout:
                # print('socket timeout')
                pass
            except Exception:
                pass

    def run(self, thread=False, prompt=None):
        """
        run the server

        :param thread: (optional) whether run server in thread.
        :param prompt: (optional) display prompt text
        :return: if thread=True, return Thread object.
        """
        if thread:
            t = threading.Thread(target=self._run, args=(prompt, ))
            t.start()
            self.is_thread = True
            return t
        else:
            self.is_thread = False
            self._run(prompt)

    def stop(self):
        """ stop the server (available when run in thread) """
        self.canceled = True
        msg = Message(random.randint(0x1A1B, 0x7FFF), QueryType.A, "stop")
        ip = '127.0.0.1' if not self.ip else self.ip
        DnsUtils.send_udp(ip, self.port, msg.to_bytes(), 200, 1, 0)

    def _query_upper_dns(self, client_address, request):
        """ find answer in upper DNS , return response bytes """
        response = DnsUtils.send_udp(self.upper_dns_server, 53, request, 500, 2)
        if response:
            self._send_response(client_address, response)
        else:
            self._send_error_response(client_address, request)

    def _send_response(self, client_address, response_bytes):
        """ send response bytes """
        self.server_socket.sendto(response_bytes, client_address)

    def _send_error_response(self, client_address, request):
        """ send error response """
        msg = Message(request)
        response_bytes = msg.response_error(ErrorCode.REFUSED)
        self._send_response(client_address, response_bytes)
