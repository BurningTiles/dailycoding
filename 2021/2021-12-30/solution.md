# Smallest Integer Divisible by K

### Python
```python
def smallestIntDivByK(k):
	if k%2==0 or k%5==0: return -1
	n, l = 1, 1
	while n%k:
		n = (n*10+1)%k
		l += 1
	return l

print(smallestIntDivByK(1))
print(smallestIntDivByK(2))
print(smallestIntDivByK(3))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int smallestIntDivByK(int k){
	if(k%2==0 or k%5==0) return -1;
	int n=1, len=1;
	while(n%k)
		n = (n*10+1)%k, ++len;
	return len;
}

signed main() {
	cout << smallestIntDivByK(1) << endl;
	cout << smallestIntDivByK(2) << endl;
	cout << smallestIntDivByK(3) << endl;
	return 0;
}
```