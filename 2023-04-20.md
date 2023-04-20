# Solution - 20 Apr

### [Percentage](https://workat.tech/problem-solving/practice/percentage)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n; cin >> n;
	double sum = 0, tmp;
	for(int i=0; i<n; i++) {
		cin >> tmp;
		sum += tmp;
	}
	printf("%.2lf%%", (sum*100/(n*80.0)));
	return 0;
}
```

### [Max in Matrix](https://workat.tech/problem-solving/practice/max-in-matrix)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int m, n, tmp, maximum=INT_MIN; cin >> m >> n;
	for(int i=0; i<m*n; i++){
		cin >> tmp;
		maximum = max(maximum, tmp);
	}
	
	cout << maximum;
	return 0;
}
```

### [Adjacent Zeros](https://workat.tech/problem-solving/practice/adjancent-zeros)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s; cin >> s;
	for(int i=1; i<s.size(); i++)
		if(s[i]=='0' && s[i-1]=='0') {
			cout << "Yes" << endl;
			return;
		}
	cout << "No" << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [Digit Sum](https://workat.tech/problem-solving/practice/digit-sum)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, sum = 0;
	cin >> n;
	while(n) {
		sum += n%10;
		n /= 10;
	}
	cout << sum << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

### [Square Sum](https://workat.tech/problem-solving/practice/square-sum)
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, ans=0;
	cin >> n;
	while(n) {
		int tmp = n%10;
		n/=10;
		ans += tmp*tmp;
	}
	cout << ans << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
```

