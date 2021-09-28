def min_operations(a, b):
	if a==b:
		return 0
	if a<=0 and b>0:
		return -1
	if a>b:
		return a-b
	if b&1==1:
		return 1+min_operations(a, b+1)
	else:
		return 1+min_operations(a, b//2)

print(min_operations(6, 20))
print(min_operations(20, 25))
print(min_operations(7, 65))
print(min_operations(20, 10))