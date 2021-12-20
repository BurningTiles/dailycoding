#include <bits/stdc++.h>
using namespace std;

string remove_outermost_parenthesis(string s){
	string ans="";
	for(int i=0, open=0; i<s.size(); i++){
		if(s[i]=='('){
			if(open) ans+=s[i];
			++open;
		}
		else{
			--open;
			if(open) ans+=s[i];
		}
	}
	return ans;
}

signed main() {
	cout << remove_outermost_parenthesis("(())()") << endl;
	cout << remove_outermost_parenthesis("(()())") << endl;
	cout << remove_outermost_parenthesis("()()()") << endl;
	return 0;
}