# Maximum Difference Between Increasing Elements

### Python
```python
def max_diff(v):
	ans, minv = -1, v[0]
	for i in range(1, len(v)):
		if v[i]<=minv:
			minv = v[i]
		else:
			ans = max([ans, v[i]-minv])
	return ans

print(max_diff([7, 1, 5, 4]))
print(max_diff([9, 4, 3, 2]))
print(max_diff([1, 5, 2, 10]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int max_diff(const vector<int> &v){
	int ans=-1, minv=v[0];
	for(int i=1; i<v.size(); i++)
		v[i]<=minv ? minv=v[i] : ans=max(ans, v[i]-minv);
	return ans;
}

signed main() {
	cout << max_diff({7, 1, 5, 4}) << endl;
	cout << max_diff({9, 4, 3, 2}) << endl;
	cout << max_diff({1, 5, 2, 10}) << endl;
	return 0;
}
```