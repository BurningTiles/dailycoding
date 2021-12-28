def has_character_map(s1, s2):
	if len(s1)!=len(s2): return False
	m = dict()
	for i in range(len(s1)):
		if s1[i] not in m or m[s1[i]]==s2[i]:
			m[s1[i]] = s2[i]
		else: return False
	return True

print(has_character_map('abc', 'def'))
print(has_character_map('aac', 'def'))