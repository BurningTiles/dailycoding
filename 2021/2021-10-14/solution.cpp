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