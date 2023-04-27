def lengthOfLongestSubstring(s):
	count = dict()
	j, ans, curLen = 0, 0, 0
	for i in range(len(s)):
		if s[i] not in count:
			count[s[i]] = 1
			curLen += 1
		else:
			while s[i] in count:
				del count[s[j]]
				curLen -= 1
				j += 1
			count[s[i]] = 1
			curLen += 1
		ans = max([ans, curLen])
	return ans

print(lengthOfLongestSubstring('abrkaabcdefghijjxxx'))