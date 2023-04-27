def pascal_triangle_row(n):
	ans, prev = [1], 1
	for i in range(1,n):
		curr = prev*(n-i)//i
		ans.append(curr)
		prev = curr
	return ans

print(pascal_triangle_row(6))