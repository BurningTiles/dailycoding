# Ways to Traverse a Grid

### Python
```python
def num_ways(n, m):
	a = [[0]*(m+1) for _ in range(n+1)]
	a[0][1] = 1
	for i in range(1, n+1):
		for j in range(1, m+1):
			a[i][j] = a[i][j-1] + a[i-1][j]
	return a[n][m]

print (num_ways(2, 2))
print (num_ways(3, 7))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int num_ways(int n, int m){
	int a[n+1][m+1] = {0};
	for(int i=0; i<=n; i++) a[i][0] = 0;
	for(int j=0; j<=m; j++) a[0][j] = 0;
	a[0][1] = 1;
	for(int i=1; i<=n; i++)
		for(int j=1; j<=m; j++)
			a[i][j] = a[i][j-1] + a[i-1][j];
	return a[n][m];
}

signed main() {
	cout << num_ways(2, 2) << endl;
	cout << num_ways(3, 7) << endl;
	return 0;
}
```