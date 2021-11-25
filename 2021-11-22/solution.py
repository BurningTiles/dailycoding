def compare(s1, s2, x):
	i=0
	while i<len(s1) and i<len(s2):
		if x[s1[i]]<x[s2[i]]: return -1
		if x[s1[i]]>x[s2[i]]: return 1
		i += 1
	if len(s1)==len(s2): return 0
	return -1 if len(s1)<len(s2) else 1

def isSorted(words, order):
	x = dict()
	for i in range(len(order)):
		x[order[i]] = i
	for i in range(1, len(words)):
		if compare(words[i-1], words[i], x)>0:
			return False
	return True

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
print(isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))