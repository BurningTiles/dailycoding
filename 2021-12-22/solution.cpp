#include <bits/stdc++.h>
using namespace std;

double mysqrt(double n) {
	double ans=1;
	while(abs(ans*ans-n)>0.0001)
		ans = (ans+(n/ans))/2;
	return int(ans*1000)/1000.0;
}

signed main() {
	cout << mysqrt(5) << endl;
	return 0;
}