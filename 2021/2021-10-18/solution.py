def generateAllSubsets(a, cur=[], n=0):
	if n==len(a):
		return [cur[:]]
	ans = generateAllSubsets(a, cur, n+1)
	cur.append(a[n])
	ans = ans+generateAllSubsets(a, cur, n+1)
	cur.pop()
	return ans

print(generateAllSubsets([1, 2, 3]))