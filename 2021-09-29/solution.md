# Shortest Distance to Character

### Python
```python
def shortest_dist(s, ch):
	n = len(s)
	ans = [int(1e9)]*n
	for i in range(n):
		if s[i]==ch:
			ans[i] = 0
	for i in range(n):
		if ans[i]==0:
			j, dist=i-1, 1
			while j>=0 and ans[j]>dist:
				ans[j] = dist
				j -= 1
				dist += 1
			dist = 1
			j=i+1
			while j<n and ans[j]>dist:
				ans[j] = dist
				j += 1
				dist += 1
	return ans

print(shortest_dist('helloworld', 'l'))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> shortest_dist(string s, char ch){
	int n = s.size();
	vector<int> ans(n, INT_MAX);
	for(int i=0; i<n; i++)
		if(s[i]==ch)
			ans[i] = 0;
	for(int i=0; i<n; i++)
		if(!ans[i]){
			int j=i-1, dist=1;
			while(j>=0 && ans[j]>dist)
				ans[j--] = dist++;
			dist = 1, j=i+1;
			while(j<n && ans[j]>dist)
				ans[j++] = dist++;
		}
	return ans;
}

signed main() {

	vector<int> ans = shortest_dist("helloworld", 'l');
	for(int i=0; i<ans.size(); i++)
		cout << ans[i] << " ";
	
	return 0;
}
```