# Complement of Base 10 Integer

### Python
```python
def bitwiseComplement(n):
	x = 1
	while n>x:
		x = x*2+1
	return x-n

print(bitwiseComplement(5))
print(bitwiseComplement(7))
print(bitwiseComplement(10))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int bitwiseComplement(int n){
	int x=1;
	while(n>x) x=x*2+1;
	return x-n;
}

signed main() {
	cout << bitwiseComplement(5) << endl;
	cout << bitwiseComplement(7) << endl;
	cout << bitwiseComplement(10) << endl;
	return 0;
}
```