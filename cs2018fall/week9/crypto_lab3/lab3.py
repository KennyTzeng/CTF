from pwn import *

r = remote("csie.ctf.tw", 10136)

# 128 bytes
A = """
cd9ee7911faad7747be5a707220cba16
6195708ad35ba8a441952d9138ca151f
d5ac33060a965402fbf4b67741494253
f824c316e610e9d65eb591f2000028e4
5177361f29a542bfe3a818649779e8a3
b3d223c7fbf1810dec842ee74b75ddae
b51ffbcc7f5113062a5b294a8254453f
b2b0b3936e11c4bb5821599396ac2dc5
""".replace("\n", "")

B = """
cd9ee7911faad7747be5a707220cba16
6195700ad35ba8a441952d9138ca151f
d5ac33060a965402fbf4b67741c94253
f824c316e610e9d65eb59172000028e4
5177361f29a542bfe3a818649779e8a3
b3d22347fbf1810dec842ee74b75ddae
b51ffbcc7f5113062a5b294a82d4443f
b2b0b3936e11c4bb5821591396ac2dc5
""".replace("\n", "")

# choose lab3
r.recvuntil("[1~3]: ")
r.sendline("3")

# block of md5 is 64 bytes
prefix = "Crypto is fun"
pad = ("20" * (64 - len(prefix)))

# register
r.recvuntil("[>] ")
r.sendline("register")
r.recvuntil("(hex): ")
r.sendline(pad + A)
r.recvuntil("Token: ")
token = r.recvuntil("\n")[:-1]

# token = head(iv+pad), body(username), tail(mac)
head, token = token[:32 + len(pad)], token[32 + len(pad):]
body, tail = token[:len(A)], token[len(A):]

# username bit-flip
body = hex(int(body, 16) ^ int(A, 16) ^ int(B, 16))[2:]
token = head + body + tail

r.recvuntil("[>] ")
r.sendline("login")
r.recvuntil("Token: ")
r.sendline(token)

r.interactive()

