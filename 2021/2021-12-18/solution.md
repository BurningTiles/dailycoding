# Numbers At Most N Given Digit Set

### Python
```python
def count(digits, n):
	num, ns, ds = str(n), len(str(n)), len(digits)
	ans = sum(pow(ds, i) for i in range(1, ns))
	for i in range(ns):
		j=0
		while j<ds and digits[j]<num[i]:
			ans += pow(ds, ns-i-1)
			j += 1
		if j>=ds or digits[j]!=num[i]: return ans
	return ans+1

print(count(["1", "3", "5", "7"], 100))
print(count(["1", "4", "9"], 1000000000))
print(count(["7"], 8))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int count(vector<string> digits, int n){
	string num = to_string(n);
	int ans=0, ns = num.size(), ds = digits.size();
	for(int i=1; i<ns; i++) ans += pow(ds, i);
	for(int i=0, j; i<ns; i++){
		for(j=0; j<ds && digits[j][0]<num[i]; j++)
			ans += pow(ds, ns-i-1);
		if(j>=ds or digits[j][0]!=num[i]) return ans;
	}
	return ans+1;
}

signed main() {
	cout << count({"1", "3", "5", "7"}, 100) << endl;
	cout << count({"1", "4", "9"}, 1000000000) << endl;
	cout << count({"7"}, 8) << endl;

	return 0;
}
```