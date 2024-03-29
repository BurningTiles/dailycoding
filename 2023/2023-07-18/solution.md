# Solution - 18 Jul 2023

---
## [1. Rotting Apples](https://workat.tech/problem-solving/practice/rotting-apples) [(LeetCode)](https://leetcode.com/problems/rotting-oranges/) 

### cpp
```cpp
int isValid(int n, int m, int i, int j) {
	return i>=0 && i<n && j>=0 && j<m;
}

int getDaysToRot(vector<vector<int> > &grid) {
	int n = grid.size(), m = grid[0].size();
	queue<vector<int>> q;
	int ones = 0;
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			if(grid[i][j]==2) q.push({i, j});
			else if(grid[i][j]==1) ++ones;
	if(!q.size() && ones) return -1;
	int ans = 0;
	while(q.size()) {
		int size = q.size();
		while(size--) {
			int i=q.front()[0], j=q.front()[1];
			q.pop();
			if(isValid(n,m, i-1, j) && grid[i-1][j]==1)
				grid[i-1][j] = 2, q.push({i-1, j});
			if(isValid(n,m, i+1, j) && grid[i+1][j]==1)
				grid[i+1][j] = 2, q.push({i+1, j});
			if(isValid(n,m, i, j-1) && grid[i][j-1]==1)
				grid[i][j-1] = 2, q.push({i, j-1});
			if(isValid(n,m, i, j+1) && grid[i][j+1]==1)
				grid[i][j+1] = 2, q.push({i, j+1});
		}
		if(q.size()) ++ans;
	}
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			if(grid[i][j]==1) return -1;
	return ans;
}
```


---
## [2. Non-Repeating Element](https://workat.tech/problem-solving/practice/non-repeating-element) [(LeetCode)](https://leetcode.com/problems/single-element-in-a-sorted-array/) 

### cpp
```cpp
// Binary search - Time complexity O(log N)
int findNonRepeatingElement(vector<int> &arr) {
	int left=0, right=arr.size()-1, ans ;
	while(left<=right) {
		if(left==right) return arr[left];
		int mid = (left + right) / 2;
		if(arr[mid]==arr[mid&1 ? mid-1 : mid+1])
			left = mid+1;
		else
			right = mid;
	}
	return -1;
}

/*
// Easy to implement - Time complexity O(N)
int findNonRepeatingElement(vector<int> &arr) {
	int ans = 0;
	for(auto &num: arr)
		ans ^= num;
	return ans;
}
*/
```
