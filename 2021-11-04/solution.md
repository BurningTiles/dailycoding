# Valid Mountain Array

### Python
```python
def validMountainArray(a):
	i = 1
	while i<len(a) and a[i]>a[i-1]:
		i += 1
	if i==1 or i==len(a):
		return False
	while i<len(a) and a[i]<a[i-1]:
		i += 1
	return i==len(a)

print(validMountainArray([1, 2, 3, 2, 1]))
print(validMountainArray([1, 2, 3]))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool validMountainArray(vector<int> a){
	int i=1;
	while(i<a.size() && a[i]>a[i-1])
		++i;
	if(i==1 || i==a.size()) 
		return false;
	while(i<a.size() && a[i]<a[i-1]) 
		++i;
	return i==a.size();
}

signed main() {
	cout << toBool(validMountainArray({1, 2, 3, 2, 1})) << endl;
	cout << toBool(validMountainArray({1, 2, 3})) << endl;
	return 0;
}
```