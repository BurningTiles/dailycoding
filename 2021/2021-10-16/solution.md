# Maximum Non Adjacent Sum

### Python
```python
def maxNonAdjacentSum(a):
	inc, exc = a[0], 0
	for i in range(1, len(a)):
		tmp = inc if inc>exc else exc
		inc = exc + a[i]
		exc = tmp
	return inc if inc>exc else exc

print(maxNonAdjacentSum([3, 4, 1, 1]))
print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
print(maxNonAdjacentSum([5, 5, 10, 100, 10, 5]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int maxNonAdjacentSum(vector<int> a){
	int include=a[0], exclude=0, tmp;
	for(int i=1; i<a.size(); i++){
		tmp = max(include, exclude);
		include = exclude + a[i];
		exclude = tmp;
	}
	return max(include, exclude);
}

signed main() {
	cout << maxNonAdjacentSum({3, 4, 1, 1}) << endl;
	cout << maxNonAdjacentSum({2, 1, 2, 7, 3}) << endl;
	cout << maxNonAdjacentSum({5, 5, 10, 100, 10, 5}) << endl;

	return 0;
}
```