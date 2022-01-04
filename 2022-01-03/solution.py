def findJudge(n, trust):
	v = [0]*(n+1)
	for t in trust:
		v[t[0]] -= 1
		v[t[1]] += 1
	for i in range(1, n+1):
		if v[i]==n-1: return i
	return -1

print(findJudge(2, [[1, 2]]))
print(findJudge(3, [[1, 3], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))