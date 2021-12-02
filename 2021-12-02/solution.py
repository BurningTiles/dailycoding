def dfs(start, adj, visited):
	visited[start] = True
	for end in adj[start]:
		if not visited[end]:
			dfs(end, adj, visited)

def isConnected(start, adj, mark):
	visited = [False]*26
	dfs(start, adj, visited)

	for i in range(26):
		if mark[i] and not visited[i]: return False
	return True

def chainedWords(words):
	mark = [False]*26
	adj = [[] for _ in range(26)]
	inBound, outBound = [0]*26, [0]*26
	for word in words:
		x=ord(word[0])-97
		y=ord(word[-1])-97
		mark[x], mark[y] = True, True
		inBound[x] += 1
		outBound[y] += 1
		adj[x].append(y)
	for i in range(26):
		if inBound[i]!=outBound[i]: return False
	return isConnected(ord(words[0][0])-97, adj, mark)
		

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))