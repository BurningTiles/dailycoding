#include <bits/stdc++.h>
using namespace std;

vector<int> find_num(vector<int> v, int val){
	int l=0, r=v.size()-1, mid;
	while(l<=r){
		mid = l+r/2;
		if(v[mid]==val) break;
		else if(v[mid]<val) l=mid+1;
		else r=mid-1;
	}
	if(l>r) return {-1, -1};
	l = r = mid;
	while(l>=0 && v[l]==val) --l;
	while(r<v.size() && v[r]==val) ++r;
	return {l+1, r-1};
}

signed main() {
	vector<int> ans = find_num({1, 1, 3, 5, 7}, 1);
	cout << ans[0] << " " << ans[1] << endl;
	ans = find_num({1, 2, 3, 4}, 5);
	cout << ans[0] << " " << ans[1] << endl;

	return 0;
}