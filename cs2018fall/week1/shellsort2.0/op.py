from pwn import *
import binascii

context.arch = "amd64"

for i in range(1,256):
	print disasm(binascii.a2b_hex(hex(i)[2:].zfill(2)))

for i in range(1,256):
	for j in range(1,256):
		print disasm(binascii.a2b_hex(hex(i)[2:].zfill(2)) + binascii.a2b_hex(hex(j)[2:].zfill(2)))
