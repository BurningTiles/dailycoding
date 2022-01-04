# Pairs of Songs With Total Durations Divisible by 60

### Python
```python
def numPairsDivisibleBy60(a):
	count, ans = [0]*60, 0
	for x in a:
		ans += count[(600-x)%60]
		count[x%60] += 1
	return ans

print(numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(numPairsDivisibleBy60([60, 60, 60]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int numPairsDivisibleBy60(vector<int> v){
	int count[60]={0}, ans=0;
	for(auto &x:v)
		ans += count[(600-x)%60],
		count[x%60]++;
	return ans;
}

signed main() {
	cout << numPairsDivisibleBy60({30, 20, 150, 100, 40}) << endl;
	cout << numPairsDivisibleBy60({60, 60, 60}) << endl;
	return 0;
}
```