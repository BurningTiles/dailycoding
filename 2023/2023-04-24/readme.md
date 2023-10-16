# Solution - 24 Apr

### [Narcissistic Number](https://workat.tech/problem-solving/practice/narcissistic-number)
```cpp
#include <bits/stdc++.h>
using namespace std;

int getSize(int n) {
	int size = 0;
	while(n){
		size++;
		n /= 10;
	}
	return size;
}

void solve() {
	int n;
	cin >> n;
	int tmp = n, size=getSize(n), sum = 0;
	while(tmp) {
		sum += pow(tmp%10, size);
		tmp /= 10;
	}
	cout << (sum==n ? "Yes" : "No") << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [Sum-Product Number](https://workat.tech/problem-solving/practice/sum-product-number)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n;
	cin >> n;
	int sum=0, mul=1, tmp=n, d;
	while(tmp) {
		d = tmp%10;
		tmp /= 10;
		sum += d;
		mul *= d;
	}
	cout << (sum*mul==n ? "Yes" : "No") << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [Gross Salary](https://workat.tech/problem-solving/practice/gross-salary)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int tt; cin >> tt;
	double hra, da, bonus, gross, mul;
	cin >> hra >> da >> bonus;
	mul = 1.0 + (hra+da+bonus)/100;
	while(tt--){
		cin >> gross;
		printf("%.2lf\n", gross*mul);
	}
	return 0;
}
```
