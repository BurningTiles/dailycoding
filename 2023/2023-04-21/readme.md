# Solution - 21 Apr

### [Armstrong Number](https://workat.tech/problem-solving/practice/armstrong-number)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, tmp, sum=0;
	cin >> n;
	tmp = n;
	while(tmp) {
		int d = tmp%10;
		tmp /= 10;
		sum += d*d*d;
	}
	cout << (n==sum ? "Yes" : "No") << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [Fibonacci Series](https://workat.tech/problem-solving/practice/fibonacci-series)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n; cin >> n;
	int a=0, b=1, sum=0;
	while(n--) {
		cout << a << " ";
		sum = a+b;
		a = b, b = sum;
	}
	cout << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [N Factorial](https://workat.tech/problem-solving/practice/n-factorial)
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;

void solve() {
	int n, ans=1;
	cin >> n;
	for(int i=2; i<=n; i++)
		ans *= i;
	cout << ans << endl;
}

signed main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```
