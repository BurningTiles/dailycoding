# Solution - 07 Sep 2023

---
## [1. Exponentiation With Modulus](https://workat.tech/problem-solving/practice/exponent-with-modulus) 

### cpp
```cpp
int getModulatedPower(int x, int y, int z) {
	long long ans = 1, a = x;
	while(y) {
		if(y&1) ans = (ans*a) % z;
		y /= 2;
		a = (a*a) % z;
	}
	return ans;
}
```
