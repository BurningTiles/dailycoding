# Room scheduling

### Python
```python
def required_rooms(lec):
	start, end = [], []
	for (s, e) in lec:
		start.append(s)
		end.append(e)
	start.sort()
	end.sort()
	ans, cur, i, j, n = 0, 0, 0, 0, len(lec)
	while i<n and j<n:
		if start[i]<end[j]:
			cur += 1
			i += 1
		else:
			cur -= 1
			j += 1
		ans = max([ans, cur])
	return ans

print(required_rooms([(30, 75), (0, 50), (60, 150)]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int required_rooms(vector<pair<int, int>> lec){
	vector<int> start, end;
	for(auto l:lec){
		start.push_back(l.first);
		end.push_back(l.second);
	}
	sort(start.begin(), start.end());
	sort(end.begin(), end.end());
	int ans=0, cur=0, i=0, j=0, n=lec.size();
	while(i<n && j<n){
		if(start[i]<end[j]){
			cur++;
			i++;
		}
		else{
			cur--;
			j++;
		}
		ans = max(cur, ans);
	}
	return ans;
}

signed main() {
	cout << required_rooms({{30, 75}, {0, 50}, {60, 150}}) << endl;
	return 0;
}
```