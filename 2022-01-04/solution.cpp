#include <bits/stdc++.h>
using namespace std;

int bitwiseComplement(int n){
	int x=1;
	while(n>x) x=x*2+1;
	return x-n;
}

signed main() {
	cout << bitwiseComplement(5) << endl;
	cout << bitwiseComplement(7) << endl;
	cout << bitwiseComplement(10) << endl;
	return 0;
}