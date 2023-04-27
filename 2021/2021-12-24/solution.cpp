#include <bits/stdc++.h>
using namespace std;

string reverseWords(string s){
	string ans="";
	int j=-1, tmp;
	for(int i=0; i<s.size(); i++)
		if(s[i]==' '){
			tmp = i-1;
			while(tmp>j) ans += s[tmp--];
			ans += " ", j=i;
		}
	tmp = s.size()-1;
	while(tmp>j) ans += s[tmp--];
	return ans;
}

signed main() {
	cout << reverseWords("The cat in the hat") << endl;
	return 0;
}