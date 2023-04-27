#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> transpose(vector<vector<int>> mat) {
	vector<vector<int>> ans;
	for(int i=0; i<mat[0].size(); i++) {
		vector<int> tmp;
		for(int j=0; j<mat.size(); j++)
			tmp.push_back(mat[j][i]);
		ans.push_back(tmp);
	}
	return ans;
}

signed main() {
	vector<vector<int>> x {
		{1, 2, 3},
		{4, 5, 6}
	};

	vector<vector<int>> ans = transpose(x);
	for(int i=0; i<ans.size(); i++){
		for(int j=0; j<ans[i].size(); j++)
			cout << ans[i][j] << " ";
		cout << endl;
	}
	return 0;
}