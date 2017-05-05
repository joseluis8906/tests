#!/usr/bin/env python

from socket import *
from random import randint

def getRandomOcteto ():
    return chr(randint(1, 255))

def sendeth(src, dst, eth_type, payload, interface = "wls4"):
  assert(len(src) == len(dst) == 6) # 48-bit ethernet addresses
  assert(len(eth_type) == 2) # 16-bit ethernet type
  s = socket(AF_PACKET, SOCK_RAW)
  s.bind((interface, 0))
  return s.send(src + dst + eth_type + payload)

if __name__ == "__main__":
  for _ in range(10):
    print("Sent %d-byte Ethernet packet on eth0" % sendeth("\xFE\xED\xFA\xCE\xBE\xEF",""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto()+""+getRandomOcteto(), "\x7A\x05", "a"*64))
