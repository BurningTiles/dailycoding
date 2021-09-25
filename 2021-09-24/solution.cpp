/**
 * Author  : BurningTiles
 * Created : 2021-09-24 21:49:36
 * Link    : BurningTiles.github.io
 * File    : solution.cpp
**/

#include <bits/stdc++.h>
using namespace std;

string multiply(string num1, string num2) {
	for(int i=0; i<num1.size(); i++) if(num1[i]<'0' || num1[i]>'9') return "NaN";
	for(int j=0; j<num2.size(); j++) if(num2[j]<'0' || num2[j]>'9') return "NaN";
	int n=num1.size(), m=num2.size(), tmp;
	string ans(n+m,'0');
	for(int i=n-1; i>=0; i--)
		for(int j=m-1; j>=0; j--){
			tmp = (num1[i]-'0')*(num2[j]-'0')+(ans[i+j+1]-'0');
			ans[i+j+1] = tmp%10+'0';
			ans[i+j] += tmp/10;
		}
	for(int i=0; i<m+n; i++)
		if(ans[i]!='0')
			return ans.substr(i);
	return "0";
}

signed main() {
	string num1, num2;
	cin >> num1 >> num2;
	cout << multiply(num1,num2);
	return 0;
}