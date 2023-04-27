def find_num(a, val):
	ans = (-1, -1)
	l, mid, r = 0, 0, len(a)-1
	while l<r:
		mid = (l+r)//2
		if a[mid]<val:
			l = mid+1
		else:
			r = mid
	if a[l]!=val:
		return ans
	else:
		ans = (l, -1)
	r = len(a)-1
	while l<r:
		mid = (l+r)//2+1
		if a[mid]>val:
			r = mid-1
		else:
			l = mid
	ans = (ans[0], r)
	return ans
	

print(find_num([1, 1, 3, 5, 7], 1))
print(find_num([1, 2, 3, 4], 5))