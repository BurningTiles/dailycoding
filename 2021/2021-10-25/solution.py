def zigzag(s, rows)->str:
	ans = ""
	a, b = (rows-2)*2, 2
	for i in range(rows):
		if i==0 or i==rows-1:
			for j in range(i, len(s), (rows-1)*2):
				ans += s[j]
			continue
		alter = False
		for j in range(i, len(s), b if alter else a):
			ans += s[j]
		a-=2
		b+=2
	return ans

print(zigzag("INSTAGRAMISAWESOME", 4))