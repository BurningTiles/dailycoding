# Connected colors in a grid

### Python
```python
class Grid:
	def __init__(self, grid):
		self.a = grid

	def area(self, i, j, v):
		if i<0 or i>=len(v) or j<0 or j>=len(v[0]) or v[i][j] or self.a[i][j]==0:
			return 0
		v[i][j] = True
		return self.a[i][j] + self.area(i-1, j, v) + self.area(i+1, j, v) + self.area(i, j+1, v) + self.area(i, j-1, v)

	def max_connected_colors(self):
		visited = [[False for j in range(len(self.a[0]))] for i in range(len(self.a))]
		ans = 0
		for i in range(len(self.a)):
			for j in range(len(self.a[0])):
				ans = max([ans, self.area(i, j, visited)])
		return ans

grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int area(int i, int j, vector<vector<bool>> &v, vector<vector<int>> a){
	if(i<0 || i>=v.size() || j<0 || j>=v[0].size() || v[i][j] || !a[i][j])
		return 0;
	v[i][j] = true;
	return a[i][j] + area(i-1, j, v, a) + area(i+1, j, v, a) 
	               + area(i, j+1, v, a) + area(i, j-1, v, a);
}

int max_connected_colors(vector<vector<int>> a){
	vector<vector<bool>> visited;
	vector<bool> tmp(a[0].size(), false);
	for(int i=0; i<a.size(); i++) visited.push_back(tmp);
	int ans = 0;
	for(int i=0; i<a.size(); i++)
		for(int j=0; j<a[0].size(); j++)
			ans = max(ans, area(i, j, visited, a));
	return ans;
}

signed main() {
	cout << max_connected_colors({
		{1, 0, 0, 1},
		{1, 1, 1, 1},
		{0, 1, 0, 0}
	});

	return 0;
}
```