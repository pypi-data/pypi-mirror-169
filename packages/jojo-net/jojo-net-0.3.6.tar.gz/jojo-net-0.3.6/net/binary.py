#
# Read/write binary data in memory or data in a file
#


import os
import struct
import random


class Binary:
    """ Read/write binary data in memory or data in a file """

    BIG_ENDIAN = 1
    LITTLE_ENDIAN = 0

    def __init__(self, data_or_file=None, offset=None, length=None, endian='big'):
        """
        create a Buffer object

        :param data_or_file:  (optional) bytes or filename or file-like object
        :param offset:        (optional) offset in bytes to start read
        :param length:  (optional) length of data in bytes
        :param endian:  (optional) endian mode, should be either 'big' or 'little'
        """
        self.offset = 0
        ''' current offset of bytes for read/write '''

        self.endian = Binary.LITTLE_ENDIAN
        ''' endian mode, 1 for big endian, 0 for little endian '''

        if str(endian).lower() == 'big' or str(endian) == '1':
            self.endian = Binary.BIG_ENDIAN

        self.file = None
        ''' file object of data'''

        self.file_start_offset = None

        self.buf = bytearray()
        ''' byte array buffer '''

        if data_or_file is not None:
            self._load(data_or_file, offset, length)

    def __getitem__(self, index):
        return self.buf[index]

    def __setitem__(self, index, value):
        self.ensure_length(index + 1)
        self.buf[index] = value
        self.offset = max(index + 1, self.offset)

    def __len__(self):
        return self.size

    def __del__(self):
        self.close()

    def _load(self, data_or_file, offset, length):
        """
        load from data or file

        :param data_or_file:  bytes or filename or file-like object
        :param offset:        offset in bytes to start read
        :param length:        length of data in bytes
        :return: None
        """
        if offset is None:
            offset = 0

        if isinstance(data_or_file, bytearray):
            if length is None:
                length = len(data_or_file) - offset
            self.buf = data_or_file[offset: offset + length]
            self.offset = len(self.buf)
        elif isinstance(data_or_file, bytes):
            self._load(bytearray(data_or_file), offset, length)
        elif isinstance(data_or_file, Binary):
            self._load(data_or_file.buf, offset, length)
        elif isinstance(data_or_file, str):
            mode = 'ab+'
            if isinstance(offset, str):
                mode = offset
            self.file = open(data_or_file, mode)
            self.offset = 0
            self.file.seek(0)
            self.file_start_offset = self.file.tell()
        elif self._is_file_object(data_or_file):
            self.file = data_or_file
            self.offset = 0
            self.file_start_offset = self.file.tell()
        else:
            raise ValueError("expect bytes but %s is found" % repr(type(data_or_file)))

    # noinspection PyMethodMayBeStatic
    def _is_file_object(self, data):
        """ whether data is file-like object """
        if hasattr(data, "read") and hasattr(data, "write") \
                and hasattr(data, "tell") and hasattr(data, "seek"):
            return True

    def clear(self):
        """ clear all data """
        self.buf = bytearray()
        self.offset = 0

    def close(self):
        """ close the file """
        if self.file:
            self.file.close()
            self.file = None

    def ensure_length(self, minimum_length):
        """ ensure the length to match the minimum length """
        if not self.file:
            if len(self.buf) < minimum_length:
                new_buf = bytes(minimum_length - len(self.buf))
                self.buf = self.buf + new_buf

    def put_byte(self, b, offset):
        """ put a byte at specified offset """
        self.put_uint8(b, offset)

    def put_uint8(self, b, offset):
        """ put a 1-byte unsigned integer at specified offset """
        if self.file:
            if self.file.tell() != self.file_start_offset + offset:
                self.file.seek(self.file_start_offset + offset)
            self.file.write(bytes([b & 0xFF]))
        else:
            self.ensure_length(offset + 1)
            self.buf[offset] = b & 0xFF

    def put_int8(self, b, offset):
        """ put a 1-byte integer at specified offset """
        self.put_uint8(b & 0xFF, offset)

    def put_char(self, c, offset):
        """ put a char at specified offset """
        num = ord(c)
        if num < 256:
            self.put_uint8(c, offset)
        elif num < 65536:
            self.put_int16(c, offset)
        else:
            self.put_int32(c, offset)

    def put_int16(self, n, offset):
        """ put a 2-bytes integer at specified offset """
        self.ensure_length(offset + 2)
        b0 = (n & 0xFF00) >> 8
        b1 = (n & 0xFF)
        if not self.endian:
            b0, b1 = b1, b0
        self.put_uint8(b0, offset)
        self.put_uint8(b1, offset + 1)

    def put_uint16(self, n, offset):
        """ put a 2-bytes unsigned integer at specified offset """
        self.ensure_length(offset + 2)
        b0 = (n & 0xFF00) >> 8
        b1 = (n & 0xFF)
        if not self.endian:
            b0, b1 = b1, b0
        self.put_uint8(b0, offset)
        self.put_uint8(b1, offset + 1)

    def put_uint32(self, n, offset):
        """ put a 4-bytes unsigned integer at specified offset """
        self.ensure_length(offset + 4)
        b0 = (n & 0xFF000000) >> 24
        b1 = (n & 0xFF0000) >> 16
        b2 = (n & 0xFF00) >> 8
        b3 = (n & 0x00FF)
        if not self.endian:
            b0, b1, b2, b3 = b3, b2, b1, b0
        self.put_uint8(b0, offset)
        self.put_uint8(b1, offset + 1)
        self.put_uint8(b2, offset + 2)
        self.put_uint8(b3, offset + 3)

    def put_int32(self, n, offset):
        """ put a 4-bytes integer at specified offset """
        self.put_uint32(n, offset)

    def put_uint64(self, n, offset):
        """ put a 8-bytes unsigned integer at specified offset """
        self.ensure_length(offset + 4)
        b0 = (n & 0xFF00000000000000) >> 56
        b1 = (n & 0xFF000000000000) >> 48
        b2 = (n & 0xFF0000000000) >> 40
        b3 = (n & 0xFF00000000) >> 32
        b4 = (n & 0xFF000000) >> 24
        b5 = (n & 0xFF0000) >> 16
        b6 = (n & 0xFF00) >> 8
        b7 = (n & 0xFF)
        if not self.endian:
            b0, b1, b2, b3, b4, b5, b6, b7 = b7, b6, b5, b4, b3, b2, b1, b0
        self.put_uint8(b0, offset)
        self.put_uint8(b1, offset + 1)
        self.put_uint8(b2, offset + 2)
        self.put_uint8(b3, offset + 3)
        self.put_uint8(b4, offset + 4)
        self.put_uint8(b5, offset + 5)
        self.put_uint8(b6, offset + 6)
        self.put_uint8(b7, offset + 7)

    def put_int64(self, n, offset):
        """ put a 8-bytes integer at specified offset """
        self.put_uint64(n, offset)

    def put_float32(self, n, offset):
        """ put a 4-bytes float(single) at specified offset """
        self.ensure_length(offset + 4)
        prefix = '>' if self.endian else '<'
        bs = struct.pack(prefix + 'f', n)
        self.put_bytes(bs, offset, 4)

    def put_float64(self, n, offset):
        """ put a 8-bytes float(double) at specified offset """
        self.ensure_length(offset + 8)
        prefix = '>' if self.endian else '<'
        bs = struct.pack(prefix + 'd', n)
        self.put_bytes(bs, offset, 8)

    def put_bytes(self, src_bytes, offset=None, length=None, src_offset=None):
        """
        put multiple bytes from src at src_offset to specified offset

        :param src_bytes:     source bytes
        :param offset:  the offset to put
        :param length:  (optional)length of data in bytes.
        :param src_offset: src offset to start
        :return: return length of bytes which is written
        """
        if offset is None:
            offset = 0

        if src_offset is None:
            src_offset = 0

        if length is None:
            length = len(src_bytes) - src_offset

        self.ensure_length(offset + length)

        if isinstance(src_bytes, Binary):
            src_bytes = bytes(src_bytes.buf)
        elif isinstance(src_bytes, bytearray):
            src_bytes = bytes(src_bytes)

        if self.file:
            if self.file.tell() != self.file_start_offset + offset:
                self.file.seek(self.file_start_offset + offset)
            self.file.write(src_bytes[src_offset: src_offset + length])
        else:
            for i in range(length):
                self.buf[offset + i] = src_bytes[src_offset + i]

        return length

    def put_string(self, s, offset, end_zero=True):
        """
        put a string at specified offset
        :param s:     the string
        :param offset: the offset
        :param end_zero: (optional)whether put a byte of zero after string
        :return: return length of bytes which is written.
        """
        old_off = offset
        # put each char in the string
        for i in range(len(s)):
            c = s[i]
            num = ord(c)
            if num < 256:
                self.put_uint8(num, offset)
                offset += 1
            elif num < 65536:
                self.put_uint16(num, offset)
                offset += 2
            else:
                self.put_uint32(num, offset)
                offset += 4

        # put ending zero
        if end_zero:
            self.put_uint8(0, offset)
            offset += 1

        return offset - old_off

    def write_byte(self, b):
        """ write a byte, return self """
        return self.write_uint8(b & 0xFF)

    def write_int8(self, b):
        """ write a 1-byte integer, return self """
        self.put_uint8(b, self.offset)
        self.offset += 1
        return self

    def write_uint8(self, b):
        """ write a 1-byte unsigned integer, return self """
        self.put_uint8(b, self.offset)
        self.offset += 1
        return self

    def write_char(self, c):
        """ write a char, return length of bytes which is written.  """
        old_off = self.offset
        num = ord(c)
        if num < 256:
            self.put_uint8(num, self.offset)
            self.offset += 1
        elif num < 65536:
            self.put_uint16(num, self.offset)
            self.offset += 2
        else:
            self.put_uint32(num, self.offset)
            self.offset += 4
        return self.offset - old_off

    def write_int16(self, n):
        """ write 2-bytes integer, return self """
        self.put_int16(n, self.offset)
        self.offset += 2
        return self

    def write_uint16(self, n):
        """ write 2-bytes unsigned integer, return self """
        self.put_uint16(n, self.offset)
        self.offset += 2
        return self

    def write_int32(self, n):
        """ write 4-bytes integer, return self """
        self.put_int32(n, self.offset)
        self.offset += 4
        return self

    def write_uint32(self, n):
        """ write 4-bytes unsigned integer, return self """
        self.put_uint32(n, self.offset)
        self.offset += 4
        return self

    def write_int64(self, n):
        """ write 8-bytes integer, return self """
        self.put_int64(n, self.offset)
        self.offset += 8
        return self

    def write_uint64(self, n):
        """ write 8-bytes unsigned integer, return self """
        self.put_uint64(n, self.offset)
        self.offset += 8
        return self

    def write_float32(self, n):
        """ write 4-bytes float(single), return self """
        self.put_float32(n, self.offset)
        self.offset += 4
        return self

    def write_float64(self, n):
        """ write 8-bytes float(double), return self """
        self.put_float64(n, self.offset)
        self.offset += 8
        return self

    def write_bytes(self, src, length=None, src_offset=None):
        """ write bytes, return self """
        length = self.put_bytes(src, self.offset, length=length, src_offset=src_offset)
        self.offset += length
        return self

    def write_string(self, s, end_zero=True):
        """ write string, return self """
        for i in range(len(s)):
            c = s[i]
            self.write_char(c)
        if end_zero:
            self.write_uint8(0)
        return self

    def write_domain_name(self, name):
        """ write domain name in style of DNS protocol, return self """
        arr = name.split(".")
        for i in range(len(arr)):
            word = arr[i]
            self.write_uint8(len(word))
            self.write_string(word, end_zero=False)
        self.write_uint8(0)
        return self

    def read_domain_name(self):
        """ read domain name in style of DNS protocol, return string """
        name = ""
        count = 0
        off = self.offset

        length = self.get_uint8(off)
        off += 1
        self.offset = max(off, self.offset)
        while length > 0:
            if (length & 0xC0) == 0xC0:
                # it is a compression, calc new offset
                b0 = length & 0x3F
                b1 = self.get_uint8(off)
                off += 1
                self.offset = max(off, self.offset)
                off = (b0 << 8) | b1  # new offset
                # get length from new offset
                length = self.get_uint8(off)
                off += 1
                self.offset = max(off, self.offset)
                continue
            else:
                if count > 0:
                    name += "."

                for i in range(length):
                    name += chr(self.get_uint8(off))
                    off += 1

                count += 1
                length = self.get_uint8(off)
                off += 1
                self.offset = max(off, self.offset)

        return name

    def get_byte(self, offset):
        """ get a byte at specified offset """
        return self.get_uint8(offset)

    def get_uint8(self, offset):
        """ get a 1-byte unsigned integer at specified offset """
        if self.file:
            if self.file.tell() != self.file_start_offset + offset:
                self.file.seek(self.file_start_offset + offset)
            bs = self.file.read(1)
            return bs[0]
        else:
            return self.buf[offset]

    def get_int8(self, offset):
        """ get a 1-byte integer at specified offset """
        b = self.get_uint8(offset)
        positive = (b & 0x80) == 0
        if positive:
            return b
        else:
            n = (~b) & 0xFF
            n = - (n + 1)
            return n

    def get_uint16(self, offset):
        """ get a 2-bytes unsigned integer at specified offset """
        b0 = self.get_uint8(offset)
        b1 = self.get_uint8(offset + 1)
        if not self.endian:
            b0, b1 = b1, b0
        return ((b0 & 0xFF) << 8) | b1

    def get_int16(self, offset):
        """ get a 2-bytes integer at specified offset """
        b0 = self.get_uint8(offset)
        b1 = self.get_uint8(offset + 1)
        if not self.endian:
            b0, b1 = b1, b0
        positive = (b0 & 0x80) == 0
        if positive:
            return (b0 << 8) | b1
        else:
            n = (b0 << 8) | b1
            n = (~n) & 0xFFFF
            n = -(n + 1)
            return n

    def get_uint32(self, offset):
        """ get a 4-bytes unsigned integer at specified offset """
        b0 = self.get_uint8(offset)
        b1 = self.get_uint8(offset + 1)
        b2 = self.get_uint8(offset + 2)
        b3 = self.get_uint8(offset + 3)
        if not self.endian:
            b0, b1, b2, b3 = b3, b2, b1, b0
        return ((b0 & 0xFF) << 24) | ((b1 & 0xFF) << 16) | ((b2 & 0xFF) << 8) | b3

    def get_int32(self, offset):
        """ get a 4-bytes  integer at specified offset """
        b0 = self.get_uint8(offset)
        b1 = self.get_uint8(offset + 1)
        b2 = self.get_uint8(offset + 2)
        b3 = self.get_uint8(offset + 3)
        if not self.endian:
            b0, b1, b2, b3 = b3, b2, b1, b0
        positive = (b0 & 0x80) == 0
        if positive:
            return ((b0 & 0x7F) << 24) | (b1 << 16) | (b2 << 8) | b3
        else:
            n = (b0 << 24) | (b1 << 16) | (b2 << 8) | b3
            n = (~n) & 0xFFFFFFFF
            n = -(n + 1)
            return n

    def get_int64(self, offset):
        """ get a 8-bytes integer at specified offset """
        b0 = self.get_uint8(offset)
        b1 = self.get_uint8(offset + 1)
        b2 = self.get_uint8(offset + 2)
        b3 = self.get_uint8(offset + 3)
        b4 = self.get_uint8(offset + 4)
        b5 = self.get_uint8(offset + 5)
        b6 = self.get_uint8(offset + 6)
        b7 = self.get_uint8(offset + 7)
        if not self.endian:
            b0, b1, b2, b3, b4, b5, b6, b7 = b7, b6, b5, b4, b3, b2, b1, b0
        positive = (b0 & 0x80) == 0
        n = ((b0 & 0xFF) << 56) | \
            ((b1 & 0xFF) << 48) | \
            ((b2 & 0xFF) << 40) | \
            ((b3 & 0xFF) << 32) | \
            ((b4 & 0xFF) << 24) | \
            ((b5 & 0xFF) << 16) | \
            ((b6 & 0xFF) << 8) | \
            (b7 & 0xFF)
        if positive:
            return n
        else:
            n = (~n) & 0xFFFFFFFFFFFFFFFF
            n = -(n + 1)
            return n

    def get_uint64(self, offset):
        """ get a 8-bytes unsigned integer at specified offset """
        b0 = self.get_uint8(offset)
        b1 = self.get_uint8(offset + 1)
        b2 = self.get_uint8(offset + 2)
        b3 = self.get_uint8(offset + 3)
        b4 = self.get_uint8(offset + 4)
        b5 = self.get_uint8(offset + 5)
        b6 = self.get_uint8(offset + 6)
        b7 = self.get_uint8(offset + 7)
        if not self.endian:
            b0, b1, b2, b3, b4, b5, b6, b7 = b7, b6, b5, b4, b3, b2, b1, b0

        return ((b0 & 0xFF) << 56) | \
               ((b1 & 0xFF) << 48) | \
               ((b2 & 0xFF) << 40) | \
               ((b3 & 0xFF) << 32) | \
               ((b4 & 0xFF) << 24) | \
               ((b5 & 0xFF) << 16) | \
               ((b6 & 0xFF) << 8) | \
               (b7 & 0xFF)

    def get_float32(self, offset):
        """ get a 4-bytes float (single) at specified offset """
        bs = self.get_bytes(offset, 4)
        prefix = '>' if self.endian else '<'
        ret = struct.unpack(prefix + 'f', bs)
        if isinstance(ret, tuple) and len(ret) > 0:
            return ret[0]
        else:
            raise ValueError("cannot read float")

    def get_float64(self, offset):
        """ get a 8-bytes float (double) at specified offset """
        bs = self.get_bytes(offset, 8)
        prefix = '>' if self.endian else '<'
        ret = struct.unpack(prefix + 'd', bs)
        if isinstance(ret, tuple) and len(ret) > 0:
            return ret[0]
        else:
            raise ValueError("cannot read float")

    def get_string(self, off, encoding="utf-8", return_length=False):
        """
        get a string at specified offset.

        :param off:    the offset
        :param encoding:  (optional) text encoding
        :param return_length: (optional)whether return length of bytes.
        :return: if return_length=False, return string.
                if return_length=True, return (string, length)
        """
        length = 0
        if self.file:  # read string from file
            # seek offset
            if self.file.tell() != self.file_start_offset + off:
                self.file.seek(self.file_start_offset + off)
            # read a byte
            result = bytearray()
            read_bytes = self.file.read(1)
            length += 1
            # while not zero, read more bytes
            while len(read_bytes) == 1 and read_bytes[0] != 0:
                result += read_bytes
                read_bytes = self.file.read(1)
                length += 1
            result = bytes(result)
        else:
            # read string from self.buf
            i = off
            while i < len(self.buf) and self.buf[i] != 0:
                i += 1
            result = self.buf[off: i]
            result = bytes(result)
            length = i - off
            if i < len(self.buf):
                length += 1
        # convert result to string
        s = result.decode(encoding)
        if return_length:
            return s, length
        else:
            return s

    def get_bytes(self, offset=None, length=None):
        """ get bytes at specified offset """
        if offset is None:
            offset = 0

        if self.file:
            if self.file.tell() != self.file_start_offset + offset:
                self.file.seek(self.file_start_offset + offset)
            bs = self.file.read(length)
            if len(bs) != length:
                raise IOError("no enough bytes to read")
        else:
            if length is None:
                length = self.offset - offset
            bs = self.buf[offset: offset + length]
            if len(bs) != length:
                raise IOError("no enough bytes to read")
        return bytes(bs)

    def read_byte(self):
        """ read a byte """
        return self.read_uint8()

    def read_uint8(self):
        """ read a 1-byte unsigned integer """
        b = self.get_uint8(self.offset)
        self.offset += 1
        return b

    def read_int8(self):
        """ read a 1-byte integer """
        b = self.get_int8(self.offset)
        self.offset += 1
        return b

    def read_uint16(self):
        """ read a 2-bytes unsigned integer """
        n = self.get_uint16(self.offset)
        self.offset += 2
        return n

    def read_int16(self):
        """ read a 2-bytes integer """
        n = self.get_int16(self.offset)
        self.offset += 2
        return n

    def read_uint32(self):
        """ read a 4-bytes unsigned integer """
        n = self.get_uint32(self.offset)
        self.offset += 4
        return n

    def read_int32(self):
        """ read a 4-bytes integer """
        n = self.get_int32(self.offset)
        self.offset += 4
        return n

    def read_uint64(self):
        """ read a 8-bytes unsigned integer """
        n = self.get_uint64(self.offset)
        self.offset += 4
        return n

    def read_int64(self):
        """ read a 8-bytes integer """
        n = self.get_int64(self.offset)
        self.offset += 4
        return n

    def read_float32(self):
        """ read 4-bytes float(single) """
        n = self.get_float32(self.offset)
        self.offset += 4
        return n

    def read_float64(self):
        """ read 4-bytes float(double) """
        n = self.get_float64(self.offset)
        self.offset += 8
        return n

    def read_string(self, encoding="utf-8"):
        """ read a string """
        result, length = self.get_string(self.offset, encoding, return_length=True)
        self.offset += length
        return result

    def read_bytes(self, length):
        """ read multiple bytes of specified length """
        bs = self.get_bytes(self.offset, length)
        self.offset += len(bs)
        return bs

    @property
    def size(self):
        """ return the size of the data """
        if self.file:
            cur_offset = self.file.tell()
            self.file.seek(0, os.SEEK_END)
            end_offset = self.file.tell()
            self.file.seek(cur_offset)
            return end_offset - self.file_start_offset
        else:
            return self.offset

    @property
    def capacity(self):
        """ return the capacity of the buffer """
        if self.file:
            return self.size
        else:
            return len(self.buf)

    def substr(self, start_off, end_off=None):
        """ return a part of bytes"""

        if not self.file:
            if end_off is None:
                end_off = self.offset
            bs = self.buf[start_off: end_off]
            return bytes(bs)
        else:
            if self.file.tell() != self.file_start_offset + start_off:
                self.file.seek(self.file_start_offset + start_off)

            if end_off is None:
                return self.file.read()
            else:
                return self.file.read(end_off - start_off)

    def to_hex(self, sep='', column=None, prefix=False):
        """
        convert to hex string

        :param sep:     (optional) separator chars
        :param column:  (optional) how many column per row
        :param prefix:  (optional) whether has prefix '0x'
        :return: return hex string
        """
        bs = self.to_bytes()
        ret = ''
        for index, b in enumerate(bs):
            if index > 0:
                if sep:
                    ret += sep
                if column and (index % column == 0):
                    ret += '\n'
            s = hex(b).strip('0x')
            if len(s) == 0:
                s = '00'
            elif len(s) == 1:
                s = '0' + s

            if prefix is True:
                s = '0x' + s

            ret += s

        return ret

    def to_bytes(self):
        """ convert to bytes """
        return self.get_bytes(0, self.capacity)

    def __repr__(self):
        if not self.file:
            return repr(bytes(self.buf))
        else:
            return repr(self.file)


class Field:
    """ Field is an element in a Structure """
    def __init__(self):
        self._bit_count = None
        self._unsigned = None
        self._value = None
        self._struct_obj = None

    @property
    def value(self):
        """ get/set value of the field """
        if self._value is None:
            if hasattr(self, '_default_value'):
                return self._default_value
            if self.bit_count is not None:
                return 0
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def bit_count(self):
        """ bit count of the field """
        if self._bit_count is not None:
            return self._bit_count
        else:
            # extract number from class name
            class_name = type(self).__name__
            length = len(class_name)
            num = ''
            for i in range(length):
                c = class_name[length - i - 1]
                if '0' <= c <= '9':
                    num = c + num
                else:
                    if num:
                        self._bit_count = int(num)
                        return self._bit_count
                    else:
                        return None

    @property
    def is_unsigned(self):
        """ whether the field is unsigned """
        if self._unsigned is not None:
            return self._unsigned
        else:
            class_name = type(self).__name__
            if len(class_name) > 0:
                c = class_name[:1].lower()
                self._unsigned = (c == 'u')
            return self._unsigned

    # noinspection PyMethodMayBeStatic
    def _get_byte_offset(self, data, offset):
        """ return byte offset of specified offset(bit) """
        if not isinstance(data, Binary):
            raise ValueError("expect Binary object but %s is found" % repr(type(data)))

        byte_offset = int(offset / 8)
        bit_offset = offset % 8

        if bit_offset != 0:
            raise ValueError("offset must be a multiple of 8")

        return byte_offset

    def read_binary(self, data, offset):
        """
        read field value from binary data

        :param data:    Binary object
        :param offset:  bit offset where to start read
        :return: return (offset, data), where offset is bit offset after read
        """
        if not isinstance(data, Binary):
            raise ValueError("expect Binary object but %s is found" % repr(type(data)))

        if self.bit_count is None:
            self._value = None
            return offset, data

        byte_offset = int(offset / 8)
        bit_offset = offset % 8

        if self.bit_count < 8:
            # read bits
            b = data.get_uint8(byte_offset)
            mask = 0xFF << self.bit_count
            mask = (~mask) & 0xFF
            mask = mask << (8 - bit_offset - self.bit_count)
            v = b & mask
            v = v >> (8 - bit_offset - self.bit_count)
            self._value = v
            return offset + self.bit_count, data

        if bit_offset > 0:
            raise ValueError("offset must be a multiple of 8")

        if self.bit_count == 8:
            if self.is_unsigned:
                self._value = data.get_uint8(byte_offset)
            else:
                self._value = data.get_int8(byte_offset)
            end_off = byte_offset * 8 + 8
        elif self.bit_count == 16:
            if self.is_unsigned:
                self._value = data.get_uint16(byte_offset)
            else:
                self._value = data.get_int16(byte_offset)
            end_off = byte_offset * 8 + 16
        elif self.bit_count == 32:
            if self.is_unsigned:
                self._value = data.get_uint32(byte_offset)
            else:
                self._value = data.get_int32(byte_offset)
            end_off = byte_offset * 8 + 32
        elif self.bit_count == 64:
            if self.is_unsigned:
                self._value = data.get_uint64(byte_offset)
            else:
                self._value = data.get_int64(byte_offset)
            end_off = byte_offset * 8 + 64
        else:
            raise ValueError("field size %s is invalid" % self.bit_count)

        return end_off, data

    def write_binary(self, data, offset):
        """
        write field value to binary data

        :param data:   Binary object
        :param offset: bit offset where to start write
        :return: return (offset, data), where offset is bit offset after write
        """
        if not isinstance(data, Binary):
            raise ValueError("expect Binary object but %s is found" % repr(type(data)))

        if self.bit_count is None:
            return offset, data

        byte_offset = int(offset / 8)
        bit_offset = offset % 8

        if self.bit_count < 8:
            # set bits
            data.ensure_length(byte_offset + 1)
            b = data.get_uint8(byte_offset)
            mask = 0xFF << self.bit_count
            mask = (~mask) & 0xFF
            val = self.value & mask
            val = val << (8 - bit_offset - self.bit_count)
            b = (b | val) & 0xFF
            data.put_uint8(b, byte_offset)
            end_off = offset + self.bit_count
            return end_off, data

        if bit_offset > 0:
            raise ValueError("offset must be a multiple of 8")

        if self.bit_count == 8:
            if self.is_unsigned:
                data.put_uint8(self.value, byte_offset)
            else:
                data.put_int8(self.value, byte_offset)
            end_off = byte_offset * 8 + 8
        elif self.bit_count == 16:
            if self.is_unsigned:
                data.put_uint16(self.value, byte_offset)
            else:
                data.put_int16(self.value, byte_offset)
            end_off = byte_offset * 8 + 16
        elif self.bit_count == 32:
            if self.is_unsigned:
                data.put_uint32(self.value, byte_offset)
            else:
                data.put_int32(self.value, byte_offset)
            end_off = byte_offset * 8 + 32
        elif self.bit_count == 64:
            if self.is_unsigned:
                data.put_uint64(self.value, byte_offset)
            else:
                data.put_int64(self.value, byte_offset)
            end_off = byte_offset * 8 + 64
        else:
            raise ValueError("field size %s is invalid" % self.bit_count)

        return end_off, data


# noinspection PyPep8
class Bit1(Field): pass
class Bit2(Field): pass
class Bit3(Field): pass
class Bit4(Field): pass
class Bit5(Field): pass
class Bit6(Field): pass
class Bit7(Field): pass
class Int8(Field): pass
class Uint8(Field): pass
class Int16(Field): pass
class Uint16(Field): pass
class Int32(Field): pass
class Uint32(Field): pass
class Int64(Field): pass
class Uint64(Field): pass
class Pointer32(Field): pass
class Pointer64(Field): pass


class Float32(Field):
    """ Field of 4-bytes float (single) """

    def read_binary(self, data: Binary, offset, encoding="utf-8"):
        """ read the string at specified offset, return bit offset, data """
        byte_offset = self._get_byte_offset(data, offset)
        self.value = data.get_float32(byte_offset)
        end_off = (byte_offset + 4) * 8
        return end_off, data

    def write_binary(self, data: Binary, offset, encoding="utf-8"):
        """ write the string to specified offset, return bit offset, data """
        byte_offset = self._get_byte_offset(data, offset)
        n = 0 if self.value is None else self.value
        data.put_float32(n, byte_offset)
        end_off = (byte_offset + 4) * 8
        return end_off, data


class Float64(Field):
    """ Field of 8-bytes float (double) """

    def read_binary(self, data: Binary, offset, encoding="utf-8"):
        """ read the string at specified offset, return bit offset, data """
        byte_offset = self._get_byte_offset(data, offset)
        self.value = data.get_float64(byte_offset)
        end_off = (byte_offset + 8) * 8
        return end_off, data

    def write_binary(self, data: Binary, offset, encoding="utf-8"):
        """ write the string to specified offset, return bit offset, data """
        byte_offset = self._get_byte_offset(data, offset)
        n = 0 if self.value is None else self.value
        data.put_float64(n, byte_offset)
        end_off = (byte_offset + 8) * 8
        return end_off, data


class String(Field):
    """ Field of zero-ended string """
    _default_value = ''

    def read_binary(self, data, offset, encoding="utf-8"):
        """ read the string at specified offset, return offset, data """
        byte_offset = self._get_byte_offset(data, offset)
        self.value, length = data.get_string(byte_offset, encoding, return_length=True)
        end_off = (byte_offset + length) * 8
        return end_off, data

    def write_binary(self, data, offset, encoding="utf-8"):
        """ write the string to specified offset, return offset, data """
        byte_offset = self._get_byte_offset(data, offset)
        s = '' if self.value is None else self.value
        bs = s.encode(encoding)
        data.put_bytes(bs, byte_offset)
        data.put_uint8(0, byte_offset + len(bs))
        end_off = (byte_offset + len(bs) + 1) * 8
        return end_off, data


class DomainName(Field):
    """ Field of domain main in DNS style """
    _default_value = ''

    def read_binary(self, data, offset, encoding="utf-8"):
        byte_offset = self._get_byte_offset(data, offset)

        old_offset = data.offset
        data.offset = byte_offset

        self.value = data.read_domain_name()

        new_offset = data.offset
        data.offset = old_offset
        end_off = new_offset * 8
        return end_off, data

    def write_binary(self, data, offset, encoding="utf-8"):
        byte_offset = self._get_byte_offset(data, offset)

        old_offset = data.offset
        data.offset = byte_offset

        data.write_domain_name(self.value)

        new_offset = data.offset
        data.offset = old_offset
        end_off = new_offset * 8
        return end_off, data


class Array(Field):
    def __init__(self, field=None, length=None):
        super().__init__()
        self._item_type = None
        self._length = None

        # exchange params when length is None
        if (isinstance(field, str) or isinstance(field, int)) and length is None:
            length = field
            field = None

        # validate _item_type
        if self._is_valid_item_type(field):
            self._item_type = field
        else:
            raise ValueError('expect field type but %s is found' % repr(type(field)))

        # initialize value
        self._value = [] if self._item_type is not None else b''

        # validate length
        if self._is_valid_length(length):
            self._length = length
        else:
            raise ValueError("invalid length of byte array")

    # noinspection PyMethodMayBeStatic
    def _is_valid_item_type(self, item_type):
        if item_type is None:
            return True

        if type(item_type) == type or type(item_type) == StructMetaClass:
            if Field in item_type.__bases__:
                return True
            if Structure in item_type.__bases__:
                return True

        return False

    # noinspection PyMethodMayBeStatic
    def _is_valid_length(self, length):
        if isinstance(length, str) or length is None:
            return True
        elif isinstance(length, int) and length >= 0:
            return True

    def _get_length(self):
        """ get array length """
        length = self._length
        if isinstance(length, str):
            field_name = length  # length point to another field
            if not isinstance(self._struct_obj, Structure):
                raise ValueError('variable array field with must inside a Structure')
            f = self._struct_obj._fields.get(field_name, None)  # get the field
            if not f:
                raise ValueError('field %s not found' % field_name)
            length = f.value
        return length

    def _read_items(self, data, byte_offset, length):
        """read items of the array """
        if self._item_type is None:  # item type is None
            # read bytes
            bs = data.get_bytes(byte_offset, length)
            self.value = bytearray(bs)
            end_off = (byte_offset + len(bs)) * 8
            return end_off, data
        else:
            # item type is Field or Structure
            if not self._is_valid_item_type(self._item_type):
                raise ValueError('error item type %s', repr(self._item_type))
            # read items
            self.value = []
            off = byte_offset * 8
            for i in range(length):
                obj = self._item_type()
                off, _ = obj.read_binary(data, off)
                self.value.append(obj)
            return off, data

    def _write_items_of_byte(self, data, byte_offset, length):
        if length is None:
            bs = b'' if self.value is None else bytes(self.value)
            data.put_bytes(bs, byte_offset)
            end_off = (byte_offset + len(bs)) * 8
            data.offset = int(end_off / 8)
            return end_off, data
        elif isinstance(length, int) and length >= 0:
            bs = b'' if self.value is None else self.value
            val = bytearray(bs)
            if len(val) > length:
                val = val[:length + 1]
            else:
                val += b'\0' * (length - len(val))
            bs = bytes(val)
            data.put_bytes(bs, byte_offset)
            end_off = (byte_offset + len(bs)) * 8
            data.offset = int(end_off / 8)
            return end_off, data

    def _write_items(self, data, byte_offset, length):
        if self._item_type is None:  # item type is None
            # write bytes
            return self._write_items_of_byte(data, byte_offset, length)
        else:
            # item type is Field or Structure
            # validate length of array
            if length is not None and length != len(self._value):
                raise ValueError("expect array length is %s but %s is found" %
                                 (length, len(self._value)))
            # validate item type
            if not self._is_valid_item_type(self._item_type):
                raise ValueError('error item type %s', repr(self._item_type))

            # write items
            off = byte_offset * 8
            for i in range(len(self._value)):
                obj = self._value[i]
                if not self._is_valid_item_type(type(obj)):
                    new_obj = self._item_type()
                    if isinstance(new_obj, Field):
                        new_obj.value = obj
                    elif isinstance(new_obj, Structure):
                        new_obj._from_dict(obj)
                    obj = new_obj
                off, _ = obj.write_binary(data, off)
            return off, data

    def read_binary(self, data: Binary, offset):
        byte_offset = self._get_byte_offset(data, offset)
        length = self._get_length()
        if isinstance(length, int) and length >= 0:
            return self._read_items(data, byte_offset, length)
        else:
            raise ValueError('array length %s is invalid' % repr(length))

    def write_binary(self, data: Binary, offset):
        byte_offset = self._get_byte_offset(data, offset)
        length = self._get_length()
        if length is None or isinstance(length, int):
            return self._write_items(data, byte_offset, length)
        else:
            raise ValueError('array length %s is invalid' % repr(length))


class StructMetaClass(type):
    """ Meta class for Structure """

    def __new__(mcs, name, bases, attrs):
        """
        called when class create, modify attributes of class.

        :param mcs:  the class to modify
        :param name:  the name of the class
        :param bases:  the base class of the class
        :param attrs:  the attributes of the class
        :return:
        """
        if name == 'Structure':
            return super().__new__(mcs, name, bases, attrs)

        if '_field_names' not in attrs:
            attrs['_field_names'] = []

        field_classes = dict()
        keys = list(attrs.keys())
        for key in keys:
            if key.startswith('_'):
                continue
            field = attrs[key]

            # judge whether it is a field
            is_field = False
            if type(field) == type and (Field in field.__bases__):
                is_field = True
            elif type(field) == type and (Structure in field.__bases__):
                is_field = True
            elif isinstance(field, Array):
                is_field = True

            if is_field:
                field_classes[key] = field
                attrs['_field_names'].append(key)
                attrs.pop(key)

        attrs['_field_classes'] = field_classes

        # call super __new__ to create class
        structure_cls = super().__new__(mcs, name, bases, attrs)
        return structure_cls


class Structure(object, metaclass=StructMetaClass):
    def __init__(self, data=None, offset=None):
        # create fields
        self._fields = {}
        for key in self._field_names:
            field = self._field_classes[key]
            if type(field) == type or type(field) == StructMetaClass:
                self._fields[key] = field()
            elif isinstance(field, Array):
                item_type = getattr(field, '_item_type')
                length = getattr(field, '_length')
                obj = Array(item_type, length)
                obj._struct_obj = self
                self._fields[key] = obj

        # read data
        if data:
            if isinstance(data, dict):
                self._from_dict(data)
            else:
                if isinstance(data, Binary) and offset is None:
                    offset = 0
                self.read_binary(data, offset)

    def __getattr__(self, key):
        try:
            if not key.startswith('_'):
                f = self._fields[key]
                return f.value
            else:
                # noinspection PyUnresolvedReferences
                return super().__getattr__(key)
        except KeyError:
            raise AttributeError("Attribute '%s' not exists" % key)

    def __setattr__(self, key, value):
        try:
            if not key.startswith('_'):
                f = self._fields[key]
                f.value = value
            else:
                super().__setattr__(key, value)
        except KeyError:
            raise AttributeError("Attribute '%s' not exists" % key)

    def read_binary(self, data, offset=None):
        """
        read field value from binary data

        :param data:   Binary object
        :param offset: bit offset where to start read
        :return: return (offset, data), where offset is bit offset after read
        """
        if isinstance(data, Structure):
            _, data = data.write_binary()
            offset = 0 if offset is None else offset

        # convert data to Binary object
        if not isinstance(data, Binary):
            data = Binary(data)
            offset = 0 if offset is None else offset

        # set offset
        if isinstance(offset, int):
            off = offset
        else:
            # set offset to the begin of the data
            off = data.offset * 8

        # read each field
        for name in self._field_names:
            field = self._fields[name]
            off, _ = field.read_binary(data, off)

        data.offset = int(off / 8)
        return off, data

    def write_binary(self, data=None, offset=None):
        """
        write field value to binary data

        :param data:   Binary object
        :param offset: bit offset where to start write
        :return: return (offset, data), where offset is bit offset after write
        """
        # convert data to Binary object
        if not isinstance(data, Binary):
            data = Binary(data)

        # set offset
        if isinstance(offset, int):
            off = offset
        else:
            # set offset(bits) to the end of the data
            off = len(data) * 8

        # write each field
        for name in self._field_names:
            field = self._fields[name]
            off, data = field.write_binary(data, off)

        # adjust the offset of the data
        n = int(off / 8) + 1 if off % 8 else int(off / 8)
        if data.offset < n:
            data.offset = n

        return off, data

    def to_dict(self):
        """
        convert to dictionary

        :return: return a dictionary
        """
        ret = {}
        for name in self._field_names:
            field = self._fields[name]
            if isinstance(field, Structure):
                value = field.to_dict()
            else:
                value = field.value
            ret[name] = value
        return ret

    def _from_dict(self, dict1):
        """
        read values from dictionary

        :param dict1:  dictionary object
        :return: None
        """
        for name in self._field_names:
            field = self._fields[name]
            if name in dict1:
                if isinstance(field, Structure):
                    field._from_dict(dict1[name])
                else:
                    field.value = dict1[name]

    def to_bytes(self):
        data = Binary()
        self.write_binary(data)
        return data.to_bytes()

    def _from_bytes(self, data_bytes, offset=0):
        self.read_binary(data_bytes, offset)

    def __repr__(self):
        data = {}
        for name in self._field_names:
            field = self._fields[name]
            data[name] = field.value
        return repr(data)


def new_class(fields_dict=None, **kwargs):
    """ Dynamically create a Structure class """
    def validate_field_types(dict1):
        if dict1 is not None:
            for key in dict1:
                field = dict1[key]
                if type(field) == type or type(field) == StructMetaClass or isinstance(field, Array):
                    pass
                else:
                    raise ValueError('%s should be a field type' % key)

    def random_string(length=8):
        """ return a random string """
        alpha = 'abcdefghijklmnopqrst'
        ret = ''
        for i in range(length):
            n = random.randint(0, len(alpha) - 1)
            ret += alpha[n:n + 1]
        return ret

    if fields_dict is not None and not isinstance(fields_dict, dict):
        raise ValueError('fields_list must be a dictionary')

    # get class name
    if 'class_name' in kwargs:
        class_name = kwargs.pop('class_name')
    else:
        class_name = "TmpClass_" + random_string()

    validate_field_types(fields_dict)
    validate_field_types(kwargs)

    # combine dictionary
    fields_dict = {} if fields_dict is None else fields_dict
    for k in kwargs:
        fields_dict[k] = kwargs[k]

    return type(class_name, (Structure, ), fields_dict)

