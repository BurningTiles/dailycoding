# Perfect Number

### Python
```python
import math

def checkPerfectNumber(n):
	if n==1:
		return True
	sum, sq = 1, math.ceil(n**.5)
	for i in range(2, sq):
		if n%i==0:
			sum += i + n//i
	if sq*sq==n:
		sum += sq
	return sum==n

print(checkPerfectNumber(28))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool checkPerfectNumber(int n){
	if(n==1) return true;
	int sum=1, sq= ceil(sqrt(n));
	for(int i=2; i<sq; i++)
		if(n%i==0)
			sum += i + n/i;
	if(sq*sq==n) sum += sq;
	return sum==n;
}

signed main() {
	cout << toBool(checkPerfectNumber(28)) << endl;
	return 0;
}
```