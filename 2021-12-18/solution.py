def count(digits, n):
	num, ns, ds = str(n), len(str(n)), len(digits)
	ans = sum(pow(ds, i) for i in range(1, ns))
	for i in range(ns):
		j=0
		while j<ds and digits[j]<num[i]:
			ans += pow(ds, ns-i-1)
			j += 1
		if j>=ds or digits[j]!=num[i]: return ans
	return ans+1

print(count(["1", "3", "5", "7"], 100))
print(count(["1", "4", "9"], 1000000000))
print(count(["7"], 8))