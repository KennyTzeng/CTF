from pwn import *

r = remote("csie.ctf.tw", 10136)

def register(username):
	r.recvuntil("[>] ")
	r.sendline("register")
	r.recvuntil("Username: ")
	r.sendline(username)
	r.recvuntil("Token: ")
	# token
	return r.recvuntil("\n")[:-1]

def login(token):
	r.recvuntil("[>] ")
	r.sendline("login")
	r.recvuntil("Token: ")
	r.sendline(token)

"""
................|................|................|
usr=aaaaa&admin=|N...............|
usr=aaaaaaaaaaaa|YOOOOOOOOOOOOOOO|&admin=N........|

O = 79
"""

# choose lab1
r.recvuntil("[1~3]: ")
r.sendline("1")

A = register("a" * 5)[:32]
B = register("a" * 12 + "Y" + "O" * 15)[32:64]
login(A + B * 5)

r.interactive()

