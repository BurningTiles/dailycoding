# Find the Town Judge

### Python
```python
def findJudge(n, trust):
	v = [0]*(n+1)
	for t in trust:
		v[t[0]] -= 1
		v[t[1]] += 1
	for i in range(1, n+1):
		if v[i]==n-1: return i
	return -1

print(findJudge(2, [[1, 2]]))
print(findJudge(3, [[1, 3], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int findJudge(int n, vector<vector<int>> trust){
	vector<int> v(n+1, 0);
	for(auto &t:trust)
		v[t[0]]--, v[t[1]]++;
	for(int i=1; i<=n; i++)
		if(v[i]==n-1) return i;
	return -1;
}

signed main() {
	cout << findJudge(2, { {1, 2}}) << endl;
	cout << findJudge(3, { {1, 3}, {2, 3}}) << endl;
	cout << findJudge(3, { {1, 3}, {2, 3}, {3, 1}}) << endl;
	return 0;
}
```