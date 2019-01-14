from pwn import *

r = remote("csie.ctf.tw", 10123)

for i in range(100):
	r.recvuntil("left\n")

	nums_str = r.recvuntil("\n").strip()
	nums = nums_str.split(" ")
	nums = map(int, nums)
	nums.sort()
	nums_sort_str = ""
	for num in nums:
		nums_sort_str += str(num) + " "

	r.recv()
	r.sendline(nums_sort_str)

r.interactive()

