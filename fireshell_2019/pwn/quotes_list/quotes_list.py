from pwn import *

r = remote("127.0.0.1", 8888)
context.arch = "amd64"

def create(size, data):
	r.recvuntil("> ")
	r.sendline("1")
	r.recvuntil(": ")
	r.sendline(str(size))
	r.recvuntil(": ")
	r.send(data)

def edit(idx, data):
	r.recvuntil("> ")
	r.sendline("2")
	r.recvuntil(": ")
	r.sendline(str(idx))
	r.recvuntil(": ")
	r.send(data)

def show(idx):
	r.recvuntil("> ")
	r.sendline("3")
	r.recvuntil(": ")
	r.sendline(str(idx))
	r.recvuntil(": ")
	return r.recvline()[:-1]

def delete(idx):
	r.recvuntil("> ")
	r.sendline("4")
	r.recvuntil(": ")
	r.sendline(str(idx))


r.interactive()

