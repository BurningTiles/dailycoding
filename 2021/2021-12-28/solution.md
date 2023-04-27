# Merge Intervals

### Python
```python
def merge(a):
	a.sort()
	ans, start, end = [], a[0][0], a[0][1]
	for i in range(1, len(a)):
		if a[i][0]<=end: end=max(end, a[i][1])
		else:
			ans.append([start, end])
			start = a[i][0]
			end = a[i][1]
	ans.append([start, end])
	return ans

print(merge([[1, 3],[2, 6],[8, 10],[15, 18]]))
print(merge([[1, 4],[4, 5]]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>> a){
	sort(a.begin(), a.end());
	vector<vector<int>> ans;
	int start=a[0][0], end=a[0][1];
	for(int i=1; i<a.size(); i++)
		if(a[i][0]<=end) end=max(end, a[i][1]);
		else ans.push_back({start, end}), start=a[i][0], end=a[i][1];
	ans.push_back({start, end});
	return ans;
}

void print(vector<vector<int>> a){
	cout << "[";
	for(int i=0; i<a.size(); i++){
		cout << "[";
		for(int j=0; j<a[i].size(); j++)
			cout << a[i][j] << (j==a[i].size()-1 ? "" : ", ");
		cout << (i==a.size()-1 ? "]" : "], ");
	} cout << "]\n";
}

signed main() {
	print(merge({ {1, 3}, {2, 6}, {8, 10}, {15, 18}}));
	print(merge({ {1, 4}, {4, 5}}));
	return 0;
}
```