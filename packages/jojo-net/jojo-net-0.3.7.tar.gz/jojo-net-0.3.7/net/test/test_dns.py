from net.dns import *
import unittest
import random


class TestMessage(unittest.TestCase):

    def rand(self, value_list):
        """ return a random value in the value list """
        n = random.randint(0, len(value_list)-1)
        return value_list[n]

    def test_header(self):
        for _ in range(16):
            head = Header()
            head.id = self.rand([1, 3, 13, 5])
            head.qr = self.rand([0, 1])
            head.op_code = self.rand(list(range(16)))
            head.aa = self.rand([0, 1])
            head.tc = self.rand([0, 1])
            head.rd = self.rand([0, 1])
            head.ra = self.rand([0, 1])
            head.error_code = self.rand(list(range(16)))
            head.question_count = self.rand(list(range(10)))
            head.answer_count = self.rand(list(range(10)))
            head.name_server_count = self.rand(list(range(10)))
            head.additional_count = self.rand(list(range(10)))
            _, b = head.write_binary()
            data = b.to_bytes()
            # print(b.to_hex(sep=" "), '=>', bin(bs[2]))

            h = Header(data)
            self.assertEqual(h.qr, head.qr)
            self.assertEqual(h.op_code, head.op_code)
            self.assertEqual(h.aa, head.aa)
            self.assertEqual(h.tc, head.tc)
            self.assertEqual(h.rd, head.rd)
            self.assertEqual(h.ra, head.ra)
            self.assertEqual(h.error_code, head.error_code)
            self.assertEqual(h.question_count, head.question_count)
            self.assertEqual(h.answer_count, head.answer_count)
            self.assertEqual(h.name_server_count, head.name_server_count)
            self.assertEqual(h.additional_count, head.additional_count)
            # print(h.qr, h.op_code, h.aa, h.tc, h.rd)

    def test_message(self):
        m = Message(2, QueryType.A, "www.baidu.com")
        bs = m.to_bytes()

        m = Message(bs)
        # print(m.to_hex(' '))

    def test_dns_client(self):
        client = DnsClient('114.114.114.114')
        print(client.query('A', 'jostudio.com.cn'))
        print(client.query('A', 'www.baidu.com'))
        print(client.query('aaaa', 'www.amazon.com'))
        print(client.query('ns', 'jostudio.cn'))
        print(client.query('cname', 'www.jostudio.cn'))
        print(client.query('mx', 'qq.com'))
        print(client.query('aaaa', 'www.google.com'))
        print(client.query('ptr', '8.8.8.8'))
        print(client.query('any', 'amazon.com'))
        s = client.get_ip("jostudio.com.cn")
        print(s)


if __name__ == "__main__":
    unittest.main()

