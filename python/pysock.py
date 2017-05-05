#!/usr/bin/env python

import sys
from random import randint
from socket import socket, AF_PACKET, SOCK_RAW

def getRandomOcteto ():
    return chr(randint(1, 255))

s = socket(AF_PACKET, SOCK_RAW)
s.bind(("enp0s25", 0))

# We're putting together an ethernet frame here, 
# but you could have anything you want instead
# Have a look at the 'struct' module for more 
# flexible packing/unpacking of binary data
# and 'binascii' for 32 bit CRC
src_addr = "\x6f\x8a\x00\x12\xaa\x7b"
payload = "x"*64
ethertype = "\x08\x01"

#for _ in range(int(sys.argv[1])):
i=0
while (True):
    dst_addr = ""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()
    s.send(src_addr + dst_addr + ethertype + payload)
    print ("Enviando 64 Bytes en enp0s25 %s veces" % i) 
    i+=1
