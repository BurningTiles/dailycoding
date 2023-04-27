#include <bits/stdc++.h>
using namespace std;

int area(int i, int j, vector<vector<bool>> &v, vector<vector<int>> a){
	if(i<0 || i>=v.size() || j<0 || j>=v[0].size() || v[i][j] || !a[i][j])
		return 0;
	v[i][j] = true;
	return a[i][j] + area(i-1, j, v, a) + area(i+1, j, v, a) 
	               + area(i, j+1, v, a) + area(i, j-1, v, a);
}

int max_connected_colors(vector<vector<int>> a){
	vector<vector<bool>> visited;
	vector<bool> tmp(a[0].size(), false);
	for(int i=0; i<a.size(); i++) visited.push_back(tmp);
	int ans = 0;
	for(int i=0; i<a.size(); i++)
		for(int j=0; j<a[0].size(); j++)
			ans = max(ans, area(i, j, visited, a));
	return ans;
}

signed main() {
	cout << max_connected_colors({
		{1, 0, 0, 1},
		{1, 1, 1, 1},
		{0, 1, 0, 0}
	});

	return 0;
}