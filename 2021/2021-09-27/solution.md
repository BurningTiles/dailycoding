# Intersection of Lists

### Python
```python
def intersection(list1, list2, list3):
	i,j,k = 0,0,0
	ans = []
	while i<len(list1) and j<len(list2) and k<len(list3):
		if list1[i]==list2[j]==list3[k]:
			ans.append(list1[i])
			i += 1
			j += 1
			k += 1
		elif list1[i]<list2[j]:
			i += 1
		elif list2[j]<list3[k]:
			j += 1
		else:
			k += 1
	return ans
  
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> intersection(vector<int> a, vector<int> b, vector<int> c) {
	vector<int> ans;
	int i=0, j=0, k=0;
	while(i<a.size() && j<b.size() && k<c.size()){
		if(a[i]==b[j] && b[j]==c[k]) {
			ans.push_back(a[i]);
			i++, j++, k++;
		}
		else if(a[i]<b[j])
			++i;
		else if(b[j]<c[k])
			++j;
		else
			++k;
	}
	return ans;
}

signed main() {
	vector<int> a = {1,2,3,4}, b = {2,4,6,8}, c = {3,4,5};

	vector<int> ans = intersection(a,b,c);
	for(int i=0; i<ans.size(); i++)
		cout << ans[i] << " ";

	return 0;
}
```