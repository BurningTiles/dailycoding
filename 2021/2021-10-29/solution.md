# Closest points to origin

### Python
```python
def findClosestPointsOrigin(points, k):
	v = list()
	for p in points:
		tmp = p[0]*p[0] + p[1]*p[1]
		v.append([tmp, [p[0], p[1]]])
	v.sort()
	ans = list()
	for i in range(k):
		if i>=len(v):
			break
		ans.append(v[i][1])
	return ans

print (findClosestPointsOrigin([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int>> findClosestPointsOrigin(vector<pair<int, int>> points, int k){
	vector<pair<int, pair<int, int>>> v;
	int tmp;
	for(auto p:points)
		tmp = p.first*p.first + p.second*p.second,
		v.push_back({tmp, {p.first, p.second}});
	
	sort(v.begin(), v.end());
	vector<pair<int, int>> ans;
	for(int i=0; i<k && i<v.size(); i++)
		ans.push_back(v[i].second);
	return ans;
}

void print(vector<pair<int, int>> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << "[" << v[i].first << ", " << v[i].second << "]" << (i==v.size()-1 ? "" : ", ");
	cout << "]" << endl;
}

signed main() {
	print(findClosestPointsOrigin({
		{1, 1}, {3, 3}, {2, 2}, {4, 4}, {-1, -1}
	}, 3));
	return 0;
}
```