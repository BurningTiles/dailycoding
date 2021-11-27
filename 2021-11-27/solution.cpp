#include <bits/stdc++.h>
using namespace std;

int fibonacci(int n){
	if(n<2) return n;
	int a=0, b=1, c;
	while(--n)
		c = a+b,
		a = b,
		b = c;
	return c;
}

signed main() {
	cout << fibonacci(9) << endl;
	return 0;
}