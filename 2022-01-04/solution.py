def bitwiseComplement(n):
	x = 1
	while n>x:
		x = x*2+1
	return x-n

print(bitwiseComplement(5))
print(bitwiseComplement(7))
print(bitwiseComplement(10))