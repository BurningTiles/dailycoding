# Solution - 25 Jul 2023

---
## [1. Rat In A Maze](https://workat.tech/problem-solving/practice/rat-in-maze) 

### cpp
```cpp
bool canGetCheese(vector<vector<int>> &maze, int i=0, int j=0) {
	if(i==maze.size()-1 && j==maze[i].size()-1) return true;
	
	if(i<maze.size() && j<maze[i].size()) {
		if(maze[i][j]==1) {
			maze[i][j]=0;
			return canGetCheese(maze, i+1, j) || 
				canGetCheese(maze, i, j+1);
		}
		return false;
	}
	
	return false;
}
```


---
## [2. Subsets](https://workat.tech/problem-solving/practice/subsets) [(LeetCode)](https://leetcode.com/problems/subsets/) 

### cpp
```cpp
void generate(vector<int> &A, vector<int> &cur, vector<vector<int>> &ans, int i) {
	if(i==A.size()) { ans.push_back(cur); return; }
	generate(A, cur, ans, i+1);
	cur.push_back(A[i]);
	generate(A, cur, ans, i+1);
	cur.pop_back();
}

vector<vector<int>> subsets(vector<int> &A) {
	vector<vector<int>> ans;
	vector<int> cur;
	generate(A, cur, ans, 0);
	return ans;
}
```
