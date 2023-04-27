def valid(s):
	if s[0]=='0':
		return True if len(s)==1 else False
	if len(s)==1: return True
	if len(s)==2: return (s>="10" and s<="99")
	if len(s)==3: return (s>="100" and s<="255")
	return False

def ip_addresses(s):
	n = len(s)
	ans = []
	if n<4 or n>12: return ans
	for i in range(1, 4):
		p1 = s[0:i]
		if valid(p1):
			for j in range(i+1, i+4):
				if j>=n: break
				p2 = s[i:j]
				if valid(p2):
					for k in range(j+1, j+4):
						if k>=n: break
						p3 = s[j:k]
						if valid(p3):
							p4 = s[k:]
							if valid(p4):
								ans.append(p1+'.'+p2+'.'+p3+'.'+p4)
	return ans

print(ip_addresses('1592551013'))