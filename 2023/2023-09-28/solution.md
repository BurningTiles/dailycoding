# Solution - 28 Sep 2023

---
## [1. Decode Ways](https://workat.tech/problem-solving/practice/decode-ways) 

### cpp
```cpp
#define MOD 1000000007
int numDecodings(string s) {
	long long a=1, b=0, prev='0';
	for(auto &ch: s) {
		int tmp = 0;
		if(ch != '0') tmp += a;
		if(prev=='1' || (prev=='2' && ch<'7'))
			tmp += b;
		if(!tmp) return 0;
		b = a % MOD, a = tmp % MOD, prev = ch;
	}
	return a;
}
```
