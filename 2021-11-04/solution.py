def validMountainArray(a):
	i = 1
	while i<len(a) and a[i]>a[i-1]:
		i += 1
	if i==1 or i==len(a):
		return False
	while i<len(a) and a[i]<a[i-1]:
		i += 1
	return i==len(a)

print(validMountainArray([1, 2, 3, 2, 1]))
print(validMountainArray([1, 2, 3]))