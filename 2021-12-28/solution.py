def merge(a):
	a.sort()
	ans, start, end = [], a[0][0], a[0][1]
	for i in range(1, len(a)):
		if a[i][0]<=end: end=max(end, a[i][1])
		else:
			ans.append([start, end])
			start = a[i][0]
			end = a[i][1]
	ans.append([start, end])
	return ans

print(merge([[1, 3],[2, 6],[8, 10],[15, 18]]))
print(merge([[1, 4],[4, 5]]))