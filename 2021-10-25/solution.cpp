#include <bits/stdc++.h>
using namespace std;

string zigzag(string s, int rows){
	string ans="";
	int a=(rows-2)*2, b=2;
	for(int i=0; i<rows; i++){
		if(i==0 || i==rows-1){
			for(int j=i; j<s.size(); j+=(rows-1)*2)
				ans.push_back(s[j]);
			continue;
		}
		bool alter = false;
		for(int j=i; j<s.size(); j+=(alter ? b : a), alter=!alter)
			ans.push_back(s[j]);
		a-=2, b+=2;
	}
	return ans;
}

signed main() {
	cout << zigzag("INSTAGRAMISAWESOME", 4) << endl;
	return 0;
}