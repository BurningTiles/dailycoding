def convert_to_int(s):
	negative = False
	if s[0]=='-':
		negative = True
		s = s[1:]
	
	i, ans = 0, 0
	while i<len(s):
		if s[i]>='0' and s[i]<='9':
			ans = ans*10 + ord(s[i])-ord('0')
		else:
			break
		i += 1
	if i==len(s):
		return -ans if negative else ans
	return None

print(convert_to_int('-105') + 1)