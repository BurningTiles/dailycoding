# Remove One Layer of Parenthesis

### Python
```python
def maxSquare(m):
	ans = 0
	for i in range(len(m)):
		for j in range(len(m[0])):
			if i==0 or j==0:
				m[i][j] = int(m[i][j])
			else:
				m[i][j] = 1+min(m[i-1][j], m[i][j-1], m[i-1][j-1]) if m[i][j]=='1' else 0
			ans = max(ans, m[i][j])
	return ans**2

print(maxSquare([
	["1","0","1","0","0"],
	["1","0","1","1","1"],
	["1","1","1","1","1"],
	["1","0","0","1","0"]]))
print(maxSquare([["0","1"],["1","0"]]))
print(maxSquare([["0"]]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int maxSquare(vector<vector<char>> m){
	int ans=0;
	for(int i=0; i<m.size(); i++)
		for(int j=0; j<m[0].size(); j++)
			if(i==0 or j==0)
				ans = max(ans, int(m[i][j] -= '0'));
			else
				m[i][j] = (m[i][j]=='1' ? 1+min({m[i-1][j], m[i][j-1], m[i-1][j-1]}) : 0),
				ans = max(ans, int(m[i][j]));
	return ans*ans;
}

signed main() {
	cout << maxSquare({ 
		{'1','0','1','0','0'},
		{'1','0','1','1','1'},
		{'1','1','1','1','1'},
		{'1','0','0','1','0'}}) << endl;
	cout << maxSquare({ {'0', '1'}, {'1', '0'}}) << endl;
	cout << maxSquare({ {'0'}}) << endl;

	return 0;
}
```