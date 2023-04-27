# Nth Fibonacci Number

### Python
```python
def fibonacci(n):
	if n<2: return n
	a, b, c = 0, 1, 1
	while n>1:
		n -= 1
		c = a+b
		a = b
		b = c
	return c

print(fibonacci(9))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int fibonacci(int n){
	if(n<2) return n;
	int a=0, b=1, c;
	while(--n)
		c = a+b,
		a = b,
		b = c;
	return c;
}

signed main() {
	cout << fibonacci(9) << endl;
	return 0;
}
```