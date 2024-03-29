# Solution - 21 Jun 2023

---
## [1. Edges to Adjacency Matrix](https://workat.tech/problem-solving/practice/edges-to-adjacency-matrix) 

```cpp
vector<vector<int>> edgesToMatrix(int n, vector<vector<int>> &edges) {
	vector<vector<int>> matrix(n, vector<int>(n, 0));
	for(auto &edge:edges) {
		matrix[edge[0]][edge[1]] = 1;
		matrix[edge[1]][edge[0]] = 1;
	}
	return matrix;
}
```

---
## [2. Edges to Adjacency List](https://workat.tech/problem-solving/practice/edges-to-adjacency-list) 

```cpp
vector<vector<int>> edgesToAdjList(int n, vector<vector<int>> &edges) {
	vector<vector<int>> adjList(n);
	for(auto &edge:edges) {
		adjList[edge[0]].push_back(edge[1]);
		if(edge[0]==edge[1]) continue;
		adjList[edge[1]].push_back(edge[0]);
	}
	return adjList;
}
```