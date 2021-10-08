def generate_brackets(n):
	ans = []
	if n==0:
		return [""]
	for i in range(n):
		for left in generate_brackets(i):
			for right in generate_brackets(n-1-i):
				ans.append("(" + left + ")" + right)
	return ans
  
print(generate_brackets(1))
print(generate_brackets(3))