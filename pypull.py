import sys
import ipinfo
from scapy.all import *

seen = set()

try:
   #ipinfo token goes below here in the quotes
    urtoken = ''
   #filter file supplied in terminal
    urfile = os.path.join(sys.path[0], 'filters/', sys.argv[1])

    f = open(urfile, 'r')

    if os.stat(urfile).st_size == 0:

        filters = "not icmp"
    else:

        filters = "not icmp and " + f.read()
except:
    filter_path = sys.path[0] + '/filters'
    urfilters = os.listdir(filter_path)
    print('Error, Usage: pull [filter.txt]\n')
    print('Available Filters Located in [pypyull/filters] are:\n')
   #listing the files within pypull/filters
    for f in urfilters:
        print(f'[{f}]', end=' ')
    print('\n')

else:

    def print_summary(pkt):
        if IP in pkt:
            host_src = pkt[IP].src
            if host_src not in seen:
                seen.add(host_src)
                host_sport = pkt[IP].sport
                access_token = urtoken
                handler = ipinfo.getHandler(access_token)
                match = handler.getDetails(host_src)
                city = match.details.get('city')
                region = match.details.get('region')
                strang = ('IP ' + str(host_src) + ' ' + str(host_sport) + ' (' + str(city) + ', ' + str(region) + ')')
                print(strang)
    print('Started Listening!')
    sniff(filter=filters, prn=print_summary)
