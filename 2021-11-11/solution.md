# Integer Break

### Python
```python
def integer_break(n):
	if n<4: return n-1
	ans = 1
	while n>0:
		if n==4 or n==2: return ans*n
		ans *= 3
		n -= 3
	return ans

print(integer_break(10))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int integer_break(int n){
	if(n<4) return n-1;
	int ans=1;
	while(n){
		if(n==4 || n==2) return ans*n;
		ans *= 3;
		n -= 3;
	}
	return ans;
}

signed main() {
	cout << integer_break(10) << endl;
	return 0;
}
```