# Generate all subsets

### Python
```python
def helper(nums, ans, cur=[], n=0):
	if n==len(nums): 
		ans.append(cur[:])
		return
	helper(nums, ans, cur, n+1)
	cur.append(nums[n])
	helper(nums, ans, cur, n+1)
	del cur[-1]

def generateAllSubsets(nums):
	ans=[]
	helper(nums, ans)
	return ans

print(generateAllSubsets([1, 2, 3]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

void helper(const vector<int> &nums, vector<vector<int>> &ans, vector<int> cur={}, int n=0){
	if(n==nums.size()) {
		ans.push_back(cur);
		return;
	}
	helper(nums, ans, cur, n+1);
	cur.push_back(nums[n]);
	helper(nums, ans, cur, n+1);
	cur.pop_back();
}

vector<vector<int>> generateAllSubsets(vector<int> nums){
	vector<vector<int>> ans;
	helper(nums, ans);
	return ans;
}

void print(vector<vector<int>> v){
	cout << "[";
	for(int i=0; i<v.size(); i++){
		cout << "[";
		for(int j=0; j<v[i].size(); j++)
			cout << v[i][j] << (j==v[i].size()-1 ? "" : ", ");
		cout << "]" << (i==v.size()-1 ? "" : ", ");
	}
	cout << "]" << endl;
}

signed main() {
	print(generateAllSubsets({1, 2, 3}));
	return 0;
}
```