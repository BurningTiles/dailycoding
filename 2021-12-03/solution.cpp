#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> &a, pair<int, int> &b){
	return a.second<b.second;
}

string rearrangeString(string s){
	int count[26]={0};
	for(int i=0; i<s.size(); i++)
		count[s[i]-97]++;
	vector<pair<int, int>> v;
	for(int i=0; i<26; i++)
		if(count[i]) v.push_back({i, count[i]});
	sort(v.rbegin(), v.rend(), cmp);
	int tmp=0;
	string ans="";
	for(auto x:v){
		char ch=x.first+97;
		while(x.second--){
			if(tmp<0) tmp = ans.size()-1;
			ans.insert(ans.begin()+tmp, ch);
			tmp--;
		}
	}
	for(int i=1; i<ans.size(); i++)
		if(ans[i]==ans[i-1]) return "Not Possible";
	return ans;
}

signed main() {
	cout << rearrangeString("abbccc") << endl; 
	return 0;
}