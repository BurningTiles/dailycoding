# Add Digits

### Python
```python
def addDigits(n):
	while n>9:
		tmp = 0
		while n>0:
			tmp += n%10
			n //= 10
		n = tmp
	return n

print(addDigits(159))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int addDigits(int n){
	while(n>9){
		int tmp = 0;
		while(n)
			tmp += n%10,
			n /= 10;
		n = tmp;
	}
	return n;
}

signed main() {
	cout << addDigits(159) << endl;
	return 0;
}
```