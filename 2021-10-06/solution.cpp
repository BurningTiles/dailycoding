#include <bits/stdc++.h>
using namespace std;

string longest_common_prefix(vector<string> v){
	if (v.size() == 0) return "";
	string prefix = v[0];
	for (int i=1; i<v.size(); i++){
		int j=0;
		while(j<v[i].size() && j<prefix.size() && v[i][j]==prefix[j]) j++;
		if(j==0) return "";
		prefix = prefix.substr(0,j);
	}
	return prefix;
}

signed main() {
	cout << longest_common_prefix({"helloworld", "hellokitty", "hell"}) << endl;
	cout << longest_common_prefix({"daily", "interview", "pro"}) << endl;
	return 0;
}