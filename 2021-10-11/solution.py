def find_num(a, val):
	l, mid, r = 0, 0, len(a)-1
	while l<=r:
		mid = (l+r)//2
		if a[mid]==val:
			break
		elif a[mid]<val:
			l = mid+1
		else:
			r = mid-1
	if l>r:
		return (-1, -1)
	l = r = mid
	while l>=0 and a[l]==val:
		l -= 1
	while r<len(a) and a[r]==val:
		r += 1
	return (l+1, r-1)

print(find_num([1, 1, 3, 5, 7], 1))
print(find_num([1, 2, 3, 4], 5))