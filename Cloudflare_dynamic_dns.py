#!/usr/bin/python2.7
import requests

import json

from urllib2 import urlopen
key = ""
email = ""
cname_url = "" 
# cname_url Example = "https://api.cloudflare.com/client/v4/zones/f3970711f3ddbd3868e9f1f266b2ff88/dns_records/d916f5a4c16921a37a260910ded1801c"
a_name=""

s_ip = json.load(urlopen('https://api.ipify.org/?format=json'))['ip']

parameters = {"Content-Type": "application/json", "X-Auth-Key": key, "X-Auth-Email": email}

url = (cname_url)

r = requests.get(url, headers=parameters)
data = json.loads(r.content)
#print(r.content)

print(data['result']['content'])

print (s_ip)

c_ip = data['result']['content']

d = json.dumps({"type": "A", "name": a_name, "content": s_ip})

if s_ip != c_ip:

    u = requests.put(url, headers=parameters, data=d)
