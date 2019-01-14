from pwn import *

r = remote("csie.ctf.tw", 10136)

# choose lab2
r.recvuntil("[1~3]: ")
r.sendline("2")

"""
0 = \x00 * 16

MAC(A) = ECB(CBC(A)[-16]) = CBC(A|0)[-16:] = X

MAC(A|0|X) = ECB(CBC(A|0|X)) = CBC(A|0|X|0) = CBC(0|0),IV={0}
"""

# 1 byte, padding = \x0f * 15
A = "aa"
B = "bb"
# MAC(A) = X, MAC(B) = Y
r.recvuntil(": ")
r.sendline(A)
r.recvuntil(": ")
r.sendline(B)
r.recvuntil(": ")
mac_A = r.recvuntil(" != ")[:-4]
mac_B = r.recvuntil("\n")[:-1]

# MAC(A|0|X) = MAC(B|0|Y) = CBC(0|0),IV={0}
r.recvuntil(": ")
r.sendline(A + "0f" * 0xf + "00" * 0x10 + mac_A)
r.recvuntil(": ")
r.sendline(B + "0f" * 0xf + "00" * 0x10 + mac_B)

r.interactive()

