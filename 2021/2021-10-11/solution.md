# Range Searching in a Sorted List

### Python
```python
def find_num(a, val):
	ans = (-1, -1)
	l, mid, r = 0, 0, len(a)-1
	while l<r:
		mid = (l+r)//2
		if a[mid]<val:
			l = mid+1
		else:
			r = mid
	if a[l]!=val:
		return ans
	else:
		ans = (l, -1)
	r = len(a)-1
	while l<r:
		mid = (l+r)//2+1
		if a[mid]>val:
			r = mid-1
		else:
			l = mid
	ans = (ans[0], r)
	return ans
	

print(find_num([1, 1, 3, 5, 7], 1))
print(find_num([1, 2, 3, 4], 5))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> find_num(vector<int> a, int val){
	vector<int> ans={-1, -1};
	int l=0, r=a.size()-1, mid;
	while(l<r){
		mid = (l+r)/2;
		if(a[mid]<val) l=mid+1;
		else r=mid;
	}
	if(a[l]!=val) return ans;
	else ans[0]=l;
	r = a.size()-1;
	while(l<r){
		mid = (l+r)/2+1;
		if(a[mid]>val) r=mid-1;
		else l=mid;
	}
	ans[1] = r;
	return ans;
}

signed main() {
	vector<int> ans = find_num({1, 1, 3, 5, 7}, 1);
	cout << ans[0] << " " << ans[1] << endl;
	ans = find_num({1, 2, 3, 4}, 5);
	cout << ans[0] << " " << ans[1] << endl;

	return 0;
}
```