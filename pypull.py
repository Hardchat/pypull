from scapy.all import *
import ipinfo

f = open('filter.txt', 'r')
filters = f.read()

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

sniff(filter=filters, prn=print_summary)