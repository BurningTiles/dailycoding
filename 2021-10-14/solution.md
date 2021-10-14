# Majority Element

# Using hashmap
### Python
```python
def majority_element(nums):
	count = {}
	for n in nums:
		if n in count:
			count[n] += 1
		else:
			count[n] = 1
	for key, value in count.items():
		if value>len(nums)//2:
			return key
	return "No majority element found"

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int majority_element(vector<int> nums){
	unordered_map<int, int> m;
	for(auto n:nums)
		m[n]++;
	for(auto x:m)
		if(x.second>nums.size()/2)
			return x.first;
	cout << "No majority element found" << endl;
	return -1;
}

signed main() {
	cout << majority_element({3, 5, 3, 3, 2, 4, 3});

	return 0;
}
```

# Using moore's voting algorithm
### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int find_major(vector<int> nums){
	int index=0, count=1;
	for(int i=1; i<nums.size(); i++){
		if(nums[index]==nums[i]) ++count;
		else --count;
		if(!count) {
			index = i;
			count = 1;
		}
	}
	return nums[index];
}

bool isMajority(vector<int> nums, int val){
	int count = 0;
	for(auto n:nums)
		if(n==val) ++count;
	return count>nums.size()/2;
}

int majority_element(vector<int> nums){
	int val = find_major(nums);
	if(isMajority(nums, val)) return val;
	cout << "No majority element found" << endl;
	return -1;
}

signed main() {
	cout << majority_element({3, 5, 3, 3, 2, 4, 3});

	return 0;
}
```