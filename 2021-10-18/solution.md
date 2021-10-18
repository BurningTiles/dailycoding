# Generate all subsets

### Python
```python
def generateAllSubsets(a, cur=[], n=0):
	if n==len(a):
		return [cur[:]]
	ans = generateAllSubsets(a, cur, n+1)
	cur.append(a[n])
	ans = ans+generateAllSubsets(a, cur, n+1)
	cur.pop()
	return ans

print(generateAllSubsets([1, 2, 3]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> generateAllSubsets(vector<int> a, vector<int> cur={}, int n=0){
	if(n==a.size())
		return {cur};
	vector<vector<int>> ans = generateAllSubsets(a, cur, n+1), tmp;
	cur.push_back(a[n]);
	tmp = generateAllSubsets(a, cur, n+1);
	ans.insert(ans.end(), tmp.begin(), tmp.end());
	return ans;
}

void print(vector<vector<int>> a){
	cout << "[";
	for(int i=0; i<a.size(); i++){
		cout << "[";
		for(int j=0; j<a[i].size(); j++)
			cout << a[i][j] << (j+1==a[i].size() ? "]" : ", ");
		if(!a[i].size()) cout << "]";
		cout << (i+1==a.size() ? "]" : ", ");
	}
}

signed main() {
	print(generateAllSubsets({1, 2, 3}));

	return 0;
}
```