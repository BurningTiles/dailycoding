def isValid(s):
	stk = []
	for c in s:
		if c=='(' or c=='[' or c=='{':
			stk.append(c)
		else:
			if len(stk)==0:
				return False
			elif c==']' and stk[-1]=='[': pass
			elif c==')' and stk[-1]=='(': pass
			elif c=='}' and stk[-1]=='{': pass
			else: return False
			del stk[-1]
	return len(stk)==0

print(isValid("()(){(())"))
print(isValid(""))
print(isValid("([{}])()"))