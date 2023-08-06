from net.dns import *


response = DnsUtils.send_udp(0, 53, Message('stop', 1))
# print(response)
msg = Message(response)

