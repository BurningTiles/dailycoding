def reverse_integer(n):
	ans, negative = 0, False
	if n<0:
		negative = True
		n = -n
	while n != 0:
		ans = ans*10 + n%10
		n = n//10
	return ans if not negative else -ans

print(reverse_integer(135))
print(reverse_integer(-321))