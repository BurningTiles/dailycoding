def required_rooms(lec):
	start, end = [], []
	for (s, e) in lec:
		start.append(s)
		end.append(e)
	start.sort()
	end.sort()
	ans, cur, i, j, n = 0, 0, 0, 0, len(lec)
	while i<n and j<n:
		if start[i]<end[j]:
			cur += 1
			i += 1
		else:
			cur -= 1
			j += 1
		ans = max([ans, cur])
	return ans

print(required_rooms([(30, 75), (0, 50), (60, 150)]))