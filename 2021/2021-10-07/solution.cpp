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