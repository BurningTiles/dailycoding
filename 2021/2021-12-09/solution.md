# Minimum Difference Between Highest and Lowest of K Scores

### Python
```python
def min_diff(n, k):
	n.sort()
	ans, k = n[-1]-n[0], k-1
	for i in range(k,len(n)):
		ans = min([ans, n[i]-n[i-k]])
	return ans

print(min_diff([90], 1))
print(min_diff([9, 4, 1, 7], 2))
```

### C++
```cpp
#include <bits/stdc++.h>
#define i2d vector<vector<int>>
using namespace std;

int min_diff(vector<int> v, int k){
	sort(v.begin(), v.end());
	int ans = INT_MAX; k--;
	for(int i=k; i<v.size(); i++)
		ans = min(ans, v[i]-v[i-k]);
	return ans;
}

signed main() {
	cout << min_diff({90}, 1) << endl;
	cout << min_diff({9, 4, 1, 7}, 2) << endl;
	return 0;
}
```