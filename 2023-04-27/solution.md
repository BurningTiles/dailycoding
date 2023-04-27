<!-- # Solution - 25 Apr

### [Swap Adjacent Elements](https://workat.tech/problem-solving/practice/swap-adjacent/submissions)
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n; cin >> n;
	int a[n];
	for(int i=0; i<n; i++)
		cin >> a[i];
	for(int i=0; i<n-1; i+=2)
		cout << a[i+1] << " " << a[i] << " ";
	if(n%2)
		cout << a[n-1];
	return 0;
}
```

### [Reverse Array](https://workat.tech/problem-solving/practice/reverse-array)
```cpp
#include <bits/stdc++.h>
using namespace std;

void reverse(int arr[], int n) {
	for(int i=0; i<n/2; i++)
		swap(arr[i], arr[n-i-1]);
}

int main() {
	int n; cin >> n;
	int arr[n];
	for(auto &a: arr)
		cin >> a;
	reverse(arr, n);
	for(auto &a: arr)
		cout << a << " ";
	return 0;
}
```

### [Is Sorted?](https://workat.tech/problem-solving/practice/is-sorted)
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isSorted(int arr[], int n) {
	for(int i=1; i<n; i++)
		if(arr[i]<arr[i-1])
			return false;
	return true;
}

void solve() {
	int n; cin >> n;
	int arr[n];
	for(auto &a : arr) cin >> a;
	cout << (isSorted(arr, n) ? "Yes" : "No") << endl;
}

int main() {
	int tt; cin >> tt;
	while(tt--)
		solve();
	return 0;
}
``` -->
