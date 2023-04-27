def reverseWords(s):
	ans = ""
	for s in s.split():
		ans += s[::-1]
		ans += " "
	return ans.rstrip()

print(reverseWords("The cat in the hat"))