# Solution - 27 Jun 2023

---
## [1. Row Column Zero](https://workat.tech/problem-solving/practice/row-column-zero) [(LeetCode)](https://leetcode.com/problems/set-matrix-zeroes/) 

### cpp
```cpp
void setRowColumnZeroes(vector<vector<int>> &matrix) {
	set<int> rowNo, colNo;
	for(int i=0; i<matrix.size(); i++) {
		for(int j=0; j<matrix[i].size(); j++) {
			if(matrix[i][j]==0) {
				rowNo.insert(i), colNo.insert(j);
			}
		}
	}
	for(auto &rn: rowNo) {
		for(int j=0; j<matrix[rn].size(); j++)
			matrix[rn][j] = 0;
	}
	for(auto &cn: colNo) {
		for(int i=0; i<matrix.size(); i++)
			matrix[i][cn] = 0;
	}
}
```


---
## [2. Matrix Rotation](https://workat.tech/problem-solving/practice/matrix-rotation) [(LeetCode)](https://leetcode.com/problems/rotate-image/) 

### cpp
```cpp
vector<vector<int> > rotateMatrix(vector<vector<int>> &matrix){
	int n = matrix.size(), m = matrix[0].size();
	vector<vector<int>> ans(m, vector<int>(n));
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			ans[j][i] = matrix[i][j];
	for(auto &row: ans)
		reverse(row.begin(), row.end());
	return ans;
}
```
