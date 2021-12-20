#include <bits/stdc++.h>
using namespace std;

string decodeString(string s){
	int i=0;
	string ans = "";
	while(i<s.size()){
		if(isdigit(s[i])){
			int j=i+1;
			while(j<s.size() && s[j]!='[') j++;
			int rep = stoi(s.substr(i, j-i)), open=1;
			i = ++j;
			while(open){
				if(s[j]=='[') ++open;
				else if(s[j]==']') --open;
				j++;
			}
			string reps = decodeString(s.substr(i, j-i-1));
			while(rep--) ans += reps;
			i=j;
		}
		else ans.push_back(s[i++]);
	}
	return ans;
}

signed main() {
	cout << decodeString("3[a]2[bc]") << endl;
	cout << decodeString("3[a2[c]]") << endl;
	cout << decodeString("2[abc]3[cd]ef") << endl;
	cout << decodeString("abc3[cd]xyz") << endl;
	return 0;
}