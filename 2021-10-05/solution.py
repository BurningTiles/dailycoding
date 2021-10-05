def integer_to_roman(n):
	ans = ""
	val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	for i in range(len(val)):
		while n>=val[i]:
			n -= val[i]
			ans += rom[i]
	return ans

print(integer_to_roman(1000))
print(integer_to_roman(48))
print(integer_to_roman(444))