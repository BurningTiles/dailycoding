# Solution - 20 Jun 2023

---
## [1. Adjacency List to Adjacency Matrix](https://workat.tech/problem-solving/practice/adjacency-list-to-adjacency-matrix) 

```cpp
vector<vector<int>> adjListToMatrix(int n, vector<vector<int>> &adjList) {
	vector<vector<int>> matrix(n, vector<int>(n, 0));
	for(int i=0; i<adjList.size(); i++)
		for(auto &val:adjList[i])
			matrix[i][val] = 1;
	return matrix;
}
```

---
## [2. Adjacency Matrix to Adjacency List](https://workat.tech/problem-solving/practice/adjacency-matrix-to-adjacency-list) 

```cpp
vector<vector<int>> matrixToAdjList(int n, vector<vector<int>> &matrix) {
	vector<vector<int>> adjList(n);
	for(int i=0; i<matrix.size(); i++) {
		for(int j=0; j<matrix.size(); j++)
			if(matrix[i][j])
				adjList[i].push_back(j);
	}
	return adjList;
}
```