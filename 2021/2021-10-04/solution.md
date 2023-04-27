# Reverse Integer

### Python
```python
def reverse_integer(n):
	ans, negative = 0, False
	if n<0:
		negative = True
		n = -n
	while n != 0:
		ans = ans*10 + n%10
		n = n//10
	return ans if not negative else -ans

print(reverse_integer(135))
print(reverse_integer(-321))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

int reverse_integer(int n){
	int ans=0;
	while(n)
		ans = ans*10 + n%10,
		n /= 10;
	return ans;
}

signed main() {
	cout << reverse_integer(135) << endl;
	cout << reverse_integer(-321) << endl;
	return 0;
}
```

### Java
```java
public class solution {
	public static void main(String args[]) {
		System.out.println(reverse_integer(135));
		System.out.println(reverse_integer(-321));
	}

	public static int reverse_integer(int n) {
		int ans=0;
		while(n!=0){
			ans = ans*10 + n%10;
			n /= 10;
		}
		return ans;
	}
}
```