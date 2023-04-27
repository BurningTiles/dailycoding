# Multiply

### CPP
```cpp
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
```

# Old

### CPP
```cpp
/**
 * Author  : BurningTiles
 * Created : 2021-09-24 21:49:36
 * Link    : BurningTiles.github.io
 * File    : solution.cpp
**/

#include <bits/stdc++.h>
using namespace std;

inline int toInt(char ch) {return ch-'0';}
inline char toChar(int num) {return num+'0';}

string add(string num1, string num2) {
	if(num1.size()==0) return num2;
	if(num2.size()==0) return num1;
	string ans="";
	int i=num1.size()-1, j=num2.size()-1;
	int carry=0, digit1, digit2, tmp;
	while(i>=0 && j>=0) {
		digit1=toInt(num1[i]);
		digit2=toInt(num2[j]);
		i--;
		j--;
		tmp = digit1 + digit2 + carry;
		carry = tmp / 10;
		tmp = tmp % 10;
		ans = toChar(tmp) + ans;
	}
	while(i>=0) {
		tmp = toInt(num1[i]) + carry;
		carry = 0;
		ans = toChar(tmp) + ans;
		i--;
	}
	while(j>=0) {
		tmp = toInt(num2[j]) + carry;
		carry = 0;
		ans = toChar(tmp) + ans;
		j--;
	}
	return ans;
}

string multiply(string num1, string num2) {
	for(int i=0; i<num1.size(); i++) if(num1[i]<'0' || num1[i]>'9') return "NaN";
	for(int j=0; j<num2.size(); j++) if(num2[j]<'0' || num2[j]>'9') return "NaN";
	string ans="", tmpStr;
	int digit1, digit2, tmp, carry=0;
	for(int i=num1.size()-1; i>=0; i--) {
		tmpStr = "";
		for(int j=num2.size()-1; j>=0; j--){
			digit1=toInt(num1[i]);
			digit2=toInt(num2[j]);
			tmp = digit1*digit2+carry;
			carry = tmp / 10;
			tmp = tmp % 10;
			tmpStr = toChar(tmp) + tmpStr;
		}
		if(carry){
			tmpStr = toChar(carry) + tmpStr;
			carry = 0;
		}
		for(int j=i+1; j<num1.size(); j++)
			tmpStr.push_back('0');
		ans = add(tmpStr, ans);
	}
	return ans;
}

signed main() {
	string num1, num2;
	cin >> num1 >> num2;
	cout << multiply(num1,num2);
	return 0;
}
```