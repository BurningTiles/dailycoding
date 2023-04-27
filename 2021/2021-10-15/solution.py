def one_bits(num):
	ans = 0
	while num>0:
		ans += num&1
		num >>= 1
	return ans

print(one_bits(23))