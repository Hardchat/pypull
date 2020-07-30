#!/usr/bin/python3
from scapy.all import *
import ipinfo

def print_summary(pkt):
   if IP in pkt:
      ip_src=pkt[IP].src
   if UDP in pkt:
      udp_sport=pkt[UDP].sport
      access_token = '5ebbb1dee38bf6'
      handler = ipinfo.getHandler(access_token)
      match = handler.getDetails(ip_src)
      c = match.details.get('city')
      s = match.details.get('region')
      strang = ("IP " + str(ip_src) + " " + str(udp_sport) + " " + str(c) + ", " + str(s))
      print(strang)

sniff(filter="ip", prn=print_summary)