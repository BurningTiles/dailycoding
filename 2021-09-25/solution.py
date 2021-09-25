#
# Author  : BurningTiles
# Created : 2021-09-25 02:57:25
# Link    : BurningTiles.github.io
#

def common_characters(a):
	ans = []
	flag = [True]*26
	for i in range(len(a)):
		flagStr = [False]*26
		for ch in a[i]:
			if flag[ord(ch)-97]:
				flagStr[ord(ch)-97] = True
		flag = flagStr
	for i in range(26):
		if flag[i]:
			ans.append(chr(i+97))
	return ans

n = int(input())
a = []
for i in range(n):
	a.append(input())
print(common_characters(a))