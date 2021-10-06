def longest_common_prefix(s):
	if len(s)==0:
		return ""
	prefix = s[0]
	for i in range(1,len(s)):
		j=0
		while j<len(s[i]) and j<len(prefix) and s[i][j]==prefix[j]:
			j += 1
		if j==0:
			return ""
		prefix = prefix[:j]
	return prefix

print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
print(longest_common_prefix(['daily', 'interview', 'pro']))