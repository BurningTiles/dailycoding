def rearrangeString(s):
	count = [0]*26
	for ch in s:
		count[ord(ch)-97] += 1
	chars = []
	for i in range(26):
		if count[i]>0:
			chars.append([i, count[i]])
	chars.sort(reverse=True, key=lambda x: x[1])
	tmp, ans = 0, ""
	for x in chars:
		ch = chr(x[0]+97)
		while x[1]>0:
			x[1] -= 1
			if tmp<0:
				tmp = len(ans)-1
			ans = ans[:tmp] + ch + ans[tmp:]
			tmp -= 1
	for i in range(1, len(ans)):
		if ans[i]==ans[i-1]: return "Not Possible"
	return ans

print(rearrangeString("abbccc"))