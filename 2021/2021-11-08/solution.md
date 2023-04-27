# Array of equal parts

### Python
```python
def canPick2(arr):
	if len(arr) < 5: return False
	s = [arr[0]]
	for i in range(1, len(arr)):
		s.append(s[-1]+arr[i])
	left, right = 1, len(arr)-2
	leftSum, rightSum = arr[0], arr[-1]
	while left<right:
		if leftSum==rightSum:
			if s[right-1]-s[left] == leftSum:
				return True
		if leftSum<rightSum:
			leftSum += arr[left]
			left += 1
		else:
			rightSum += arr[right]
			right -= 1
	return False

print(canPick2([2, 4, 5, 3, 3, 9, 2, 2, 2]))
print(canPick2([1, 2, 3, 4, 5]))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool canPick2(vector<int> v){
	if(v.size()<5) return false;
	vector<int> sum = {v[0]};
	for(int i=1; i<v.size(); i++)
		sum.push_back(sum.back()+v[i]);
	int left=1, right=v.size()-2;
	int leftSum = v.front(), rightSum = v.back();
	while(left<right){
		if(leftSum==rightSum)
			if(sum[right-1]-sum[left] == leftSum) return true;
		if(leftSum<rightSum)
			leftSum += v[left++];
		else
			rightSum += v[right--];
	}
	return false;
}

signed main() {
	cout << toBool(canPick2({2, 4, 5, 3, 3, 9, 2, 2, 2})) << endl;
	cout << toBool(canPick2({1, 2, 3, 4, 5})) << endl;
	return 0;
}
```