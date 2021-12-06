# Sort Integers by The Power Value

### Python
```python
def power(x):
	ans = 0
	while x!=1:
		if x%2==0:
			x //= 2
		else:
			x = x*3+1
		ans += 1
	return ans

def getKth(low, high, k):
	v = []
	for i in range(low, high+1):
		v.append([power(i), i])
	v.sort()
	return v[k-1][1]

print(getKth(12, 15, 2))
print(getKth(1, 1, 1))
print(getKth(7, 11, 4))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int power(long long x){
	int ans=0;
	while(x!=1){
		if(x%2) x = x*3+1;
		else x /= 2;
		++ans;
	}
	return ans;
}

int getKth(int low, int high, int k){
	vector<pair<int, int>> v;
	for(int i=low; i<=high; i++)
		v.push_back({power(i), i});
	sort(v.begin(), v.end());
	return v[k-1].second;
}

signed main() {
	cout << getKth(12, 15, 2) << endl;
	cout << getKth(1, 1, 1) << endl;
	cout << getKth(7, 11, 4) << endl;
	return 0;
}
```