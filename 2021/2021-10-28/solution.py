def canSpell(magazine, note):
	a = [0]*26
	for ch in magazine:
		a[ord(ch)-97] += 1
	for ch in note:
		if a[ord(ch)-97]==0:
			return False
		a[ord(ch)-97] -= 1
	return True

print(canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
print(canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))