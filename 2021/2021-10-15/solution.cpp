#include <bits/stdc++.h>
using namespace std;

int one_bits(int n){
	int ans=0;
	while(n){
		ans += n&1;
		n >>= 1;
	}
	return ans;
}

signed main() {
	cout << one_bits(23);
	return 0;
}