def findClosestPointsOrigin(points, k):
	v = list()
	for p in points:
		tmp = p[0]*p[0] + p[1]*p[1]
		v.append([tmp, [p[0], p[1]]])
	v.sort()
	ans = list()
	for i in range(k):
		if i>=len(v):
			break
		ans.append(v[i][1])
	return ans

print (findClosestPointsOrigin([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))