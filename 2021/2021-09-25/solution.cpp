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
	vector<bool> flag(26,true);
	for(int i=0; i<v.size(); i++){
		vector<bool> flagStr(26, false);
		for(int j=0; j<v[i].size(); j++)
			if(flag[v[i][j]-97])
				flagStr[v[i][j]-97] = true;
		flag = flagStr;
	}
	for(int i=0; i<26; i++)
		if(flag[i])
			ans.push_back(i+97);
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