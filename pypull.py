from scapy.all import *
import ipinfo, sys

try:
   #ipinfo token goes here in the quotes
   urtoken = ''
   #filter file supplied in terminal
   urfile = os.path.join(sys.path[0], 'filters/', sys.argv[1])
   
   f = open(urfile, 'r')
   
   filters = f.read()  

except:
   print('Error, Usage: pull [filter.txt]\n')

else:
   
   def print_summary(pkt):
      if IP in pkt:
         ip_src=pkt[IP].src
      if UDP in pkt:
         udp_sport=pkt[UDP].sport
         access_token = urtoken
         handler = ipinfo.getHandler(access_token)
         match = handler.getDetails(ip_src)
         c = match.details.get('city')
         s = match.details.get('region')
         strang = ('IP ' + str(ip_src) + ' ' + str(udp_sport) + ' ' + str(c) + ', ' + str(s))
         print(strang)

   sniff(filter=filters, prn=print_summary)
