def numPairsDivisibleBy60(a):
	count, ans = [0]*60, 0
	for x in a:
		ans += count[(600-x)%60]
		count[x%60] += 1
	return ans

print(numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(numPairsDivisibleBy60([60, 60, 60]))