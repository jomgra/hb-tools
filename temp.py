#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests as req
import sys
import datetime

resp = req.get("http://celsius.met.uu.se/data/obs_uppsala.htm")
soup = BeautifulSoup(resp.text, "html5lib")

# Temperature

r = soup(text="Temperature")
tem = r[0].next.next.text

f = open('/home/pi/hb-tools/temp.txt', 'w')
f.write(tem)
f.close()

# Humidity

r = soup(text="Air humidity")
hum = r[0].next.next.text

f = open('/home/pi/hb-tools/hum.txt', 'w')
f.write(hum)
f.close()

# Time

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

f = open('/home/pi/hb-tools/weatherhistory.csv', 'a')
f.write(time + ";" + tem+ ";" + hum + "\n")
f.close()

sys.exit()
