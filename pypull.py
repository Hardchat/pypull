from scapy.all import *
import ipinfo, sys

try:
   #ipinfo token goes below here in the quotes
   urtoken = ''
   #filter file supplied in terminal
   urfile = os.path.join(sys.path[0], 'filters/', sys.argv[1])
   
   f = open(urfile, 'r')
   
   filters = f.read()  

except:
   muhpath = sys.path[0] + '/filters'
   urfilters = os.listdir(muhpath)
   print('Error, Usage: pull [filter.txt]\n')
   print('Available Filters Located in [pypyull/filters] are:\n')
   #listing the files within pypull/filters
   for f in urfilters:
      print(f'[{f}]', end = ' ')
   print('\n')
   
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
