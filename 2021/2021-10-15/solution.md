# Number of 1 bits

### Python
```python
def one_bits(num):
	ans = 0
	while num>0:
		ans += num&1
		num >>= 1
	return ans

print(one_bits(23))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int one_bits(int n){
	int ans=0;
	while(n){
		ans += n&1;
		n >>= 1;
	}
	return ans;
}

signed main() {
	cout << one_bits(23);
	return 0;
}
```