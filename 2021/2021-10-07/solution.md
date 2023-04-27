# 4 Sum

### Python
```python
def fourSum(nums, target):
	ans, n= [], len(nums)
	nums.sort()
	for i in range(n):
		if i>0 and nums[i]==nums[i-1]:
			continue
		for j in range(i+1,n):
			if j>i+1 and nums[j]==nums[j-1]:
				continue
			left, right, t = j+1, n-1, nums[i]+nums[j]
			while left<right:
				if left>j+1 and nums[left]==nums[left-1]:
					left += 1
					continue
				tmp = t+nums[left]+nums[right]
				if tmp==target:
					ans.append([nums[i], nums[j], nums[left], nums[right]])
					left += 1
				elif tmp<target:
					left += 1
				else:
					right -= 1
	return ans

print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
print(fourSum([0, 0, 0, 0, 0], 0))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> fourSum(vector<int> nums, int target){
	vector<vector<int>> ans;
	sort(nums.begin(), nums.end());
	for(int i=0; i<nums.size(); i++){
		if(i>0 && nums[i]==nums[i-1]) continue;
		for(int j=i+1; j<nums.size(); j++){
			if(j>i+1 && nums[j]==nums[j-1]) continue;
			int left=j+1, right=nums.size()-1;
			int t = nums[i]+nums[j];
			while(left<right){
				if(left>j+1 && nums[left]==nums[left-1]){
					left++;
					continue;
				}
				int tmp = t+nums[left]+nums[right];
				if(tmp==target){
					ans.push_back({nums[i], nums[j], nums[left], nums[right]});
					++left;
				}
				else if(tmp<target) ++left;
				else --right;
			}
		}
	}
	return ans;
}

void print(vector<vector<int>> a) {
	if(!a.size()){
		cout << "Null" << endl; return;
	}

	cout << "[";
	for(int i=0; i<a.size(); i++){
		cout << "[";
		for(int j=0; j<a[i].size(); j++)
			cout << a[i][j],
			cout << (j==a[i].size()-1 ? "]" : ", ");
		cout << (i==a.size()-1 ? "]" : ", ");
	}
	cout << endl;
}

signed main() {
	print(fourSum({1, 1, -1, 0, -2, 1, -1}, 0));
	print(fourSum({3, 0, 1, -5, 4, 0, -1}, 1));
	print(fourSum({0, 0, 0, 0, 0}, 0));
	return 0;
}
```

### Java
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class solution {
	public static void main(String args[]) {
		int a[] = {1, 1, -1, 0, -2, 1, -1};
		int b[] = {3, 0, 1, -5, 4, 0, -1};
		int c[] = {0, 0, 0, 0, 0};
		System.out.println(Arrays.deepToString(fourSum(a, 0)));
		System.out.println(Arrays.deepToString(fourSum(b, 1)));
		System.out.println(Arrays.deepToString(fourSum(c, 0)));
	}

	public static int[][] fourSum(int nums[], int target) {
		List <int[]> ans = new ArrayList<int[]>();
		Arrays.sort(nums);
		for(int i=0; i<nums.length; i++){
			if(i>0 && nums[i]==nums[i-1]) continue;
			for(int j=i+1; j<nums.length; j++){
				if(j>i+1 && nums[j]==nums[j-1]) continue;
				int left=j+1, right=nums.length-1;
				int t = nums[i]+nums[j];
				while(left<right){
					if(left>j+1 && nums[left]==nums[left-1]){
						left++;
						continue;
					}
					int tmp = t+nums[left]+nums[right];
					if(tmp==target){
						int oneSolution[] = {nums[i], nums[j], nums[left], nums[right]};
						ans.add(oneSolution);
						++left;
					}
					else if(tmp<target) ++left;
					else --right;
				}
			}
		}
		int a[][] = new int[ans.size()][];
		for(int i=0; i<a.length; i++)
			a[i] = ans.get(i);
		return a;
	}
}
```

# [Referance](https://leetcode.com/problems/4sum/solution/)