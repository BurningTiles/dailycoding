# Solution - 30 Jun 2023

---
## [1. Matrix Search](https://workat.tech/problem-solving/practice/matrix-search) [(LeetCode)](https://leetcode.com/problems/search-a-2d-matrix/) 

### cpp
```cpp
bool searchMatrix(vector<vector<int>> &matrix, int key) {
	int n = matrix.size(), m = matrix[0].size(), i=0, j=n*m-1;
	while(i<=j) {
		int mid = i+(j-i)/2;
		int x = mid/m, y = mid%m;
		if(matrix[x][y]==key) return true;
		matrix[x][y]<key ? i=mid+1 : j=mid-1;
	}
	return false;
}
```


---
## [2. Median of Row-wise Sorted Matrix](https://workat.tech/problem-solving/practice/median-row-sorted-matrix) [(LeetCode)](https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/) 

### cpp
```cpp
int calculateMedianOfMatrix(vector<vector<int> > &matrix) {
	vector<int> v;
	for(auto &row:matrix)
		v.insert(v.begin(), row.begin(), row.end());
	sort(v.begin(), v.end());
	return v[v.size()/2];
}
```