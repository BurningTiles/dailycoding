#include <bits/stdc++.h>
using namespace std;

int reverse_integer(int n){
	int ans=0;
	while(n)
		ans = ans*10 + n%10,
		n /= 10;
	return ans;
}

signed main() {
	cout << reverse_integer(135) << endl;
	cout << reverse_integer(-321) << endl;
	return 0;
}