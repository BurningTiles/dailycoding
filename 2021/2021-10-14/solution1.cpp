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