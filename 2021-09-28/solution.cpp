#include <bits/stdc++.h>
using namespace std;

int min_operations(int a, int b) {
	if(a==b) return 0;
	if(a<=0 && b>0) return -1;
	if(a>b) return a-b;
	if(b&1) return 1+min_operations(a, b+1);
	else return 1+min_operations(a, b/2);
}

signed main() {
	cout << min_operations(6, 20) << endl;
	cout << min_operations(20, 25) << endl;
	cout << min_operations(7, 65) << endl;
	cout << min_operations(20, 10) << endl;
	return 0;
}