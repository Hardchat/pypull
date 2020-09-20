from scapy.all import *
import ipinfo, sys

try:
   
   urfile = sys.argv[1]
   
   f = open(urfile, 'r')
   
   filters = f.read()  

except:
   
   print('Error!\n\nUsage: pull [filter.txt]\n')

else:
   
   def print_summary(pkt):
      if IP in pkt:
         ip_src=pkt[IP].src
      if UDP in pkt:
         udp_sport=pkt[UDP].sport
         access_token = ''
         handler = ipinfo.getHandler(access_token)
         match = handler.getDetails(ip_src)
         c = match.details.get('city')
         s = match.details.get('region')
         strang = ('IP ' + str(ip_src) + ' ' + str(udp_sport) + ' ' + str(c) + ', ' + str(s))
         print(strang)

   sniff(filter=filters, prn=print_summary)
