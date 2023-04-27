def closest_3sum(a, target):
	n = len(a)
	a.sort()
	ans = None
	lowestDiff = int(1e9)
	for i in range(n):
		j,k=0,n-1,
		while j<k:
			if i==j:
				j+=1
			elif i==k:
				k-=1
			else:
				add = a[i]+a[j]+a[k]
				if abs(target-add)<lowestDiff:
					lowestDiff = abs(target-add)
					ans = [a[i], a[j], a[k]]
				if add<target:
					j+=1
				else:
					k-=1
	return ans
  
print(closest_3sum([2, 1, -5, 4], -1))