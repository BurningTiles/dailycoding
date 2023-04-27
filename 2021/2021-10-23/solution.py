class Solution:
	def findAllConcatenatedWordsInAList(self, words):
		wordsSet = set()
		for word in words: wordsSet.add(word)
		ans = []
		
		def canBreak(s):
			if not wordsSet or not s: return False
			dp = [False]* ( len(s) + 1)
			dp[0] = True
			for i in range(0, len(s)):
				for j in range(i + 1, len(s) + 1):
					if dp[i] and s[i: j] in wordsSet:
						dp[j] = True
			return dp[len(s)]
		
		for word in words:
			wordsSet.remove(word)
			if canBreak(word): ans.append(word)
			wordsSet.add(word)
		return ans

input = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]
print(Solution().findAllConcatenatedWordsInAList(input))