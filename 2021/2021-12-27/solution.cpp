#include <bits/stdc++.h>
using namespace std;

long long pow(long long x, int n) {
	long long ans=1;
	while(n){
		if(n&1) ans = n>0 ? ans*x : ans/x;
		x *= x;
		n /= 2;
	}
	return ans;
}

signed main() {
	cout << pow(5, 3) << endl;
	return 0;
}