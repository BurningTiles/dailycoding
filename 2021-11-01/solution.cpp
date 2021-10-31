#include <bits/stdc++.h>
using namespace std;

int addDigits(int n){
	int tmp;
	while(n>9){
		tmp = 0;
		while(n){
			tmp += n%10;
			n /= 10;
		}
		n = tmp;
	}
	return n;
}

signed main() {
	cout << addDigits(159) << endl;
	return 0;
}