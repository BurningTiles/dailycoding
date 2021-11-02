#include <bits/stdc++.h>
using namespace std;

vector<int> findDuplicates(vector<int> a){
	int count[a.size()+1]={0};
	for(auto &num:a)
		count[num]++;
	
	vector<int> ans;
	for(int i=1; i<=a.size(); i++)
		if(count[i]>1) ans.push_back(i);
	return ans;
}

signed main() {
	vector<int> ans = findDuplicates({4, 3, 2, 7, 8, 2, 3, 1});
	cout << "[";
	for(int i=0; i<ans.size(); i++) 
		cout << ans[i] << (i==ans.size()-1 ? "" : ", ");
	cout << "]";
	return 0;
}