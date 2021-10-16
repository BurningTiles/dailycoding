# Searching a Matrix

### Python
```python
def searchMatrix(mat, val):
	m, n = len(mat), len(mat[0])
	left, right = 0, m*n-1
	while left<=right:
		mid = (left+right)//2
		tmp = mat[mid//n][mid%n]
		if tmp==val:
			return True
		elif val>tmp:
			left = mid+1
		else:
			right = mid-1
	return False

mat = [
	[1, 3, 5, 8],
	[10, 11, 15, 16],
	[24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
print(searchMatrix(mat, 10))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int searchMatrix(vector<vector<int>> mat, int val){
	int m=mat.size(), n=mat[0].size();
	int left=0, right=m*n-1, mid, tmp;
	while(left<=right){
		mid = (left+right)/2;
		tmp = mat[mid/n][mid%n];
		if(tmp==val) 
			return true;
		else if(val>tmp)
			left = mid+1;
		else
			right = mid-1;
	}
	return false;
}

signed main() {
	vector<vector<int>> mat = {
		{1, 3, 5, 8},
		{10, 11, 15, 16},
		{24, 27, 30, 31},
	};
	cout << (searchMatrix(mat, 4) ? "true" : "false") << endl;
	cout << (searchMatrix(mat, 10) ? "true" : "false") << endl;

	return 0;
}
```