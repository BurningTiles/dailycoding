#include <bits/stdc++.h>
using namespace std;

string sum_binary(string n1, string n2) {
	string ans="";
	int i=n1.size()-1, j=n2.size()-1, sum=0;
	while(i>=0 || j>=0 || sum>0)
		sum += i>=0 ? n1[i]-'0' : 0, 
		sum += j>=0 ? n2[j]-'0' : 0, 
		ans.push_back(sum%2+'0'), 
		sum /= 2, --i, --j;
	reverse(ans.begin(), ans.end());
	return ans;
}

signed main() {
	cout << sum_binary("11101", "1011");
	
	return 0;
}