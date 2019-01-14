from pwn import *

r = remote("127.0.0.1", 8888)

raw_input('data')

r.recvuntil("===\n")
r.sendline("1234+5678")

r.interactive()

