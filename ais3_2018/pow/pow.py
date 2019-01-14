from pwn import *
import hashlib, string, itertools

chars = string.ascii_letters + string.digits
nonce = ""

r = remote("104.199.235.135", 20000)
r.recvuntil("x[:6] == '")
head = r.recv(6)
r.recv()

for s in itertools.product(chars, repeat=26):
    nonce = head + "".join(s)
#    print nonce
    if hashlib.sha256(nonce).hexdigest()[:6] == '000000':
        break

r.sendline(nonce)
r.interactive()


