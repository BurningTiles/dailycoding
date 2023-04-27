#include <bits/stdc++.h>
using namespace std;

int smallestIntDivByK(int k){
	if(k%2==0 or k%5==0) return -1;
	int n=1, len=1;
	while(n%k)
		n = (n*10+1)%k, ++len;
	return len;
}

signed main() {
	cout << smallestIntDivByK(1) << endl;
	cout << smallestIntDivByK(2) << endl;
	cout << smallestIntDivByK(3) << endl;
	return 0;
}