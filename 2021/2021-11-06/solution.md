# Three Equal Sums

### Python
```python
def canThreePartsEqualSum(nums):
	if len(nums)<3: return False
	reqSum, curSum, count = 0, 0, 0
	for num in nums:
		reqSum += num
	if reqSum%3>0:
		return False
	reqSum = reqSum//3
	for num in nums:
		curSum += num
		if(curSum == reqSum):
			curSum = 0
			count += 1
		if count==3: return True
	return False

print(canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool canThreePartsEqualSum(vector<int> a){
	if(a.size()<3) return false;
	int sum=0, count=0, currentSum=0;
	for(auto x:a) sum += x;
	if(sum%3) return false;
	sum /= 3;
	for(auto x:a){
		currentSum += x;
		if(currentSum==sum){
			currentSum = 0;
			count++;
		}
		if(count==3) return true;
	}
	return false;
}

signed main() {
	cout << toBool(canThreePartsEqualSum({0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1})) << endl;
	return 0;
}
```