def word_search(m, word):
	r, c, n = len(m), len(m[0]), len(word)
	for i in range(r):
		for j in range(c):
			if m[i][j]!=word[0]: continue
			if j+n<=c:
				k=1
				while k<n:
					if m[i][j+k]!=word[k]:
						break
					k += 1
				if k==n:
					return True
			if i+n<=r:
				k=1
				while k<n:
					if m[i+k][j]!=word[k]:
						break
					k += 1
				if k==n:
					return True
	return False

matrix = [
	['F', 'A', 'C', 'I'],
	['O', 'B', 'Q', 'P'],
	['A', 'N', 'O', 'B'],
	['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))