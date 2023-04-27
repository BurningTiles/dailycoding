#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int> &comb, int target, int cur, vector<vector<int>> &counter, vector<vector<int>> &ans){
	if(target==0) ans.push_back(comb);
	if(target<=0) return;
	for(int i=cur; i<counter.size(); i++){
		int val = counter[i][0], n = counter[i][1];
		if(n<=0)
			continue;
		comb.push_back(val);
		counter[i][1]--;
		backtrack(comb, target-val, i, counter, ans);
		counter[i][1]++;
		comb.pop_back();
	}
}

vector<vector<int>> sum_combinations(vector<int> a, int target){
	vector<vector<int>> ans;
	vector<int> comb;
	map<int, int> m;
	for(int value:a) m[value]++;
	vector<vector<int>> counter;
	for(auto x:m)
		counter.push_back({x.first, x.second});
	backtrack(comb, target, 0, counter, ans);
	return ans;
}

void print(vector<vector<int>> a){
	for(auto row:a){
		cout << "[";
		for(int i=0; i<row.size(); i++)
			cout << row[i] << (i==row.size()-1 ? "] " : ", ");
	}cout << endl;
}

signed main() {
	print(sum_combinations({10, 1, 2, 7, 6, 1, 5}, 8));
	print(sum_combinations({2, 5, 2, 1, 2}, 5));
	
	return 0;
}