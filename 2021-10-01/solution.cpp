#include <bits/stdc++.h>
using namespace std;

vector<int> closest_3sum(vector<int> a, int target) {
	vector<int> ans(3);
	int lowestDiff = 1e9;
	sort(a.begin(), a.end());
	for(int i=0; i<a.size(); i++) {
		int j=0, k=a.size()-1;
		while(j<k){
			if(j==i) ++j;
			else if(k==i) --k;
			else {
				int sum = a[i]+a[j]+a[k];
				if(abs(target-sum)<lowestDiff){
					lowestDiff = abs(target-sum);
					ans[0] = a[i];
					ans[1] = a[j];
					ans[2] = a[k];
				}
				if(sum<target) ++j;
				else --k;
			}
		}
	}
	return ans;
}

signed main() {
	vector<int> nums{2, 1, -5, 4};
	vector<int> ans = closest_3sum(nums, -1);
	cout << "[" << ans[0] << ", " << ans[1] << ", " << ans[2] << "]" << endl;
	
	return 0;
}