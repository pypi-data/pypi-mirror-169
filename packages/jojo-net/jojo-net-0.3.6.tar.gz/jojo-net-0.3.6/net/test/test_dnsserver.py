import time

from net.dns import DnsServer


def test():
    server = DnsServer(port=53)
    filename = "dns_record.txt"
    server.records.load_from_file(filename)
    server.records.add("A", "aaa.jostudio.com.cn", '192.168.100.100')
    server.records.save_to_file(filename)
    server.set_upper_dns('114.114.114.114')
    server.run(thread=False, prompt=True)
    print("end")
    time.sleep(3)
    server.stop()


test()

