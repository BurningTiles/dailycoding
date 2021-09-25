#
# Author  : BurningTiles
# Created : 2021-09-25 02:57:25
# Link    : BurningTiles.github.io
#

def common_characters(a):
	ans = []
	flag = [[False]*26 for _ in range(len(a))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			flag[i][ord(a[i][j])-97] = True
	for i in range(26):
		ch = True
		for j in range(len(a)):
			if not flag[j][i]:
				ch = False
				break
		if ch:
			ans.append(chr(i+97))
	return ans

n = int(input())
a = []
for i in range(n):
	a.append(input())
print(common_characters(a))