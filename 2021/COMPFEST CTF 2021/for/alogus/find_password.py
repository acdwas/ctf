
from Crypto.Util.number import bytes_to_long, long_to_bytes
import dpkt
from dpkt.tcp import TCP
import base64

with open('ORION-PC_150820211534.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    
    l = []

    for _, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)

        ip = eth.data
        tcp = ip.data

        if type(tcp) == TCP:

            if tcp.sport == 31678 or tcp.sport == 58775:
                if len(tcp.data) > 10:
                    l.append(tcp.data)

w = []

for i in range(0,len(l),2):
    w.append(long_to_bytes(int(base64.b64decode(l[i])) ^ bytes_to_long(l[i+1])).decode().replace(' ', '').replace('Key.space', ' ').replace('Key.shift', ''))

for i in w:
    if i.find('Key.backspace') > 0:
        while True:
            x = i.find('Key.backspace')
            tmp = i[:x-1]
            tmp += i[x+len('Key.backspace'):]
            i = tmp
            if i.find('Key.backspace') < 0:
                break
    print(i)