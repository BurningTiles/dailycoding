# Pascal's Triangle

### Python
```python
def pascal_triangle_row(n):
	ans, prev = [1], 1
	for i in range(1,n):
		curr = prev*(n-i)//i
		ans.append(curr)
		prev = curr
	return ans

print(pascal_triangle_row(6))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> pascal_triangle_row(int n) {
	vector<int> ans{1};
	int prev = 1;
	for(int i=1; i<n; i++){
		int curr = prev*(n-i)/i;
		ans.push_back(curr);
		prev = curr;
	}
	return ans;
}

signed main() {
	vector<int> ans = pascal_triangle_row(6);
	for(int i=0; i<ans.size(); i++)
		cout << ans[i] << " ";
	
	return 0;
}
```