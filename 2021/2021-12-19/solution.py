def decodeString(s):
	i, ans = 0, ""
	while i<len(s):
		if s[i]>='0' and s[i]<='9':
			j=i+1
			while j<len(s) and s[j]!='[': j+=1
			rep, openBrackets = int(s[i:j]), 1
			j += 1
			i = j
			while openBrackets>0:
				if s[j]=='[': openBrackets+=1
				elif s[j]==']': openBrackets-=1
				j += 1
			reps = decodeString(s[i:j-1])
			while rep>0:
				ans += reps
				rep -= 1
			i = j
		else:
			ans += s[i]
			i += 1
	return ans

print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
print(decodeString("abc3[cd]xyz"))