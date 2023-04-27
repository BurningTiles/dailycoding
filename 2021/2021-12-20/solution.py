def remove_outermost_parenthesis(s):
	ans, op = "", 0
	for ch in s:
		if ch=='(':
			if op: ans+=ch
			op += 1
		else:
			op -= 1
			if op: ans+=ch
	return ans

print(remove_outermost_parenthesis("(())()"))
print(remove_outermost_parenthesis("(()())"))
print(remove_outermost_parenthesis("()()()"))