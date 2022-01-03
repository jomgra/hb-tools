#!/usr/bin/env python

import urllib2
import sys

url = "http://celsius.met.uu.se/data/obs_uppsala.htm"
needle1 = "<td>Temperature</td>"
needle2 = "<td>Air humidity</td>"

response = urllib2.urlopen(url)
#print response.info()
html = response.read()
i = html.find(needle1)
s = html[i+42:i+55]
temperature = s[0:s.find("</")]
i = html.find(needle2)
s = html[i+43:i+55]
humidity = s[0:s.find("</")]

response.close() 

f = open('/home/pi/hb-tools/temp.txt', 'w')
f.write(temperature)
f.close()

f = open('/home/pi/hb-tools/hum.txt', 'w')
f.write(humidity)
f.close()

sys.exit()
