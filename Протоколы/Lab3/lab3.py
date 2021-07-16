#python3 lab3.py 8.8.8.8 edu.zaikin.su


import argparse
import binascii
import socket
import math



def dec2hex(x):
    if len(x)>0xF:
        return hex(len(x))[2:]
    else:
        return ('0' + hex(len(x))[2:])

def hex2dec(str):
    res = 0
    for i in range(len(str)):
        res += int(str[i], 16) * math.pow(16, len(str)-1 - i)
    return int(res)

def parse_answer(answer):
    global hostname_length
    ans = []
    tmp = answer[24+2*(hostname_length+1)+10:] 
    while tmp != '':
        Qtype = tmp[4:8]
        if Qtype == '0001':
            res = ''
            tmp = tmp[20:]
            rdlength = tmp[:4]
            length = hex2dec(rdlength)
            tmp = tmp[4:]
            for i in range(length):
                byte = tmp[2*i] + tmp[2*i+1]
                dec = hex2dec(byte)
                res += str(dec) + '.'
            ans.append(res[:len(res)-1])
            tmp = tmp[8:]
        else:
            rdlength = hex2dec(tmp[20:24])
            tmp = tmp[24+rdlength*2:]
    return ans


def create_type_a_message(hostname):
    header = "AA AA 01 00 00 01 00 00 00 00 00 00 "
    question = ""
    tmp = hostname.split('.')
    for i in tmp:
        lenx = dec2hex(i)
        question += (lenx + ' ')
        for j in range(len(i)):
            question +=  (binascii.b2a_hex(bytes(i[j], encoding = "utf-8")).decode('utf-8') + ' ')
    return (header + question + '00 00 01 00 01')

def send_udp_message(message, address, port):
    """send_udp_message sends a message to UDP server

    message should be a hexadecimal encoded string
    """
    message = message.replace(" ", "").replace("\n", "")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        data, _ = sock.recvfrom(4096)
    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")

'''def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return " ".join(pairs)
'''
parser = argparse.ArgumentParser(description='Lab3')

parser.add_argument('DNS_Address', action="store")
parser.add_argument("Hostname", action="store")
args = parser.parse_args()



#Hostname = 'edu.zaikin.su'
hostname_length = len(args.Hostname)
#DNS_Address = '8.8.8.8'
message = create_type_a_message(args.Hostname)
response = send_udp_message(message, args.DNS_Address, 53)
#print(format_hex(response))
answer = parse_answer(response)
for ip in answer:
    print(ip)

