#include <bits/stdc++.h>
using namespace std;

string integer_to_roman(int n){
	string ans="";
	const int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
	const string rom[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
	for(int i=0; i<13; i++)
		while(n>=val[i])
			n -= val[i],
			ans += rom[i];
	return ans;
}

signed main() {
	cout << integer_to_roman(1000) << endl;
	cout << integer_to_roman(48) << endl;
	cout << integer_to_roman(444) << endl;
	return 0;
}