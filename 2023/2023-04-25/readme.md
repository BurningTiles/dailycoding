# Solution - 25 Apr

### [Net Salary](https://workat.tech/problem-solving/practice/net-salary)
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;

void solve() {
	int n; cin >> n;
	int tmp = n;
	double tax = 0;
	if(tmp>1000000) {
		tax += (tmp-1000000) * .3;
		tmp = 1000000;
	}
	if(tmp>500000) {
		tax += (tmp-500000) * .2;
		tmp = 500000;
	}
	if(tmp>300000) {
		tax += (tmp-300000) * .05;
	}
	printf("%.2f\n", n-tax);
}

signed main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [To Upper Case](https://workat.tech/problem-solving/practice/to-upper-case)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s; cin >> s;
	for(int i=0; i<s.size(); i++)
		cout << char(s[i]-32);
	cout << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [Toggle Case](https://workat.tech/problem-solving/practice/toggle-case)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int tt; cin >> tt;
	string s;
	while(tt--){
		cin >> s;
		for(int i=0; i<s.size(); i++)
			cout << char(s[i]>96 ? s[i]-32 : s[i]+32);
		cout << endl;
	}
	return 0;
}
```
