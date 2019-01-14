from pwn import *

# r = remote("127.0.0.1", 8888)
r = remote("140.110.112.31", 2116)

r.sendafter("\n", p32(0x79487ff))
r.recvuntil(".\n")

for i in range(1000):
	print(i)
	num1 = int(r.recvuntil(" ")[:-1])
	exp = r.recvuntil(" ")[:-1]
	num2 = int(r.recvuntil(" ")[:-1])
	if exp == "+":
		ans = num1 + num2
	elif exp == "-":
		ans = num1 - num2
	elif exp == "*":
		ans = num1 * num2
	elif exp == "/":
		ans = num1 / num2
	r.sendlineafter("?", str(ans))		

r.interactive()
