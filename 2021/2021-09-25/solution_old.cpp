/**
 * Author  : BurningTiles
 * Created : 2021-09-25 02:07:34
 * Link    : BurningTiles.github.io
 * File    : solution.cpp
**/

#include <bits/stdc++.h>
using namespace std;

vector<char> common_characters(vector<string> v) {
	vector<char> ans;
	bool flag[v.size()][26]={false};
	for(int i=0; i<v.size(); i++){
		for(int j=0; j<v[i].size(); j++)
			flag[i][v[i][j]-97] = 1;
	}
	for(int i=0; i<26; i++){
		bool ch = true;
		for(int j=0; j<v.size(); j++)
			if(!flag[j][i]){
				ch = false;
				break;
			}
		if(ch) ans.push_back(i+97);
	}
	return ans;
}

signed main() {

	// input
	int n;
	cin >> n;
	vector<string> v(n);
	for(int i=0; i<n; i++)
		cin >> v[i];

	// calling function
	vector<char> ans = common_characters(v);
	n = ans.size();

	// printing output.
	cout << '[';
	for(int i=0; i<n-1; i++)
		cout << '\'' << ans[i] << "\', ";
	if(n)
		cout << '\'' << ans.back() << "\']" << endl;
	else
		cout << "]" << endl;
	
	return 0;
}