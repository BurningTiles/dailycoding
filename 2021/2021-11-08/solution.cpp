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