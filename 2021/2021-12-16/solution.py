def minHeightTrees(n, edges):
	if n==1: return [0]
	if n==2: return edges[0]
	graph, indegree, ans = [[] for _ in range(n)], [0]*n, []

	for e in edges:
		graph[e[0]].append(e[1])
		graph[e[1]].append(e[0])
		indegree[e[0]]+=1
		indegree[e[1]]+=1
	
	q = []
	for i in range(n):
		if indegree[i]==1:
			q.append(i)
			indegree[i]-=1
	
	while len(q)>0:
		s = len(q)
		ans = []
		for i in range(s):
			cur = q[0]
			del q[0]
			ans.append(cur)
			for child in graph[cur]:
				indegree[child]-=1
				if indegree[child]==1:
					q.append(child)
	return ans
	

print(minHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(minHeightTrees(6, [[3, 0],[3, 1],[3, 2],[3, 4],[5, 4]]))
print(minHeightTrees(1, []))
print(minHeightTrees(2, [[0, 1]]))