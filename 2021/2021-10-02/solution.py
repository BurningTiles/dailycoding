def sum_binary(n1, n2):
	ans = ""
	i,j,s = len(n1)-1, len(n2)-1, 0
	while i>=0 or j>=0 or s>0:
		s += int(n1[i]) if i>=0 else 0
		s += int(n2[j]) if j>=0 else 0
		ans += str(s%2)
		i -= 1
		j -= 1
		s = s//2
	return ans[::-1]
	
print(sum_binary("11101", "1011"))