#!/usr/bin/env python

import sys
from random import randint
from socket import socket, AF_PACKET, SOCK_RAW

def getRandomOcteto ():
    return chr(randint(1, 255))

s = socket(AF_PACKET, SOCK_RAW)
s.bind(("wls4", 0))

# We're putting together an ethernet frame here, 
# but you could have anything you want instead
# Have a look at the 'struct' module for more 
# flexible packing/unpacking of binary data
# and 'binascii' for 32 bit CRC
src_addr = "\x6f\x8a\x00\x12\xaa\x7b"
payload = "a"*64
ethertype = "\x08\x01"

for _ in range(25):
    dst_addr = ""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()
    s.send(src_addr + dst_addr + ethertype + payload) 
