# Solution - 08 Aug 2023

---
## [1. Consecutively Descending Integers](https://workat.tech/problem-solving/practice/consecutively-descending-integers) 

### cpp
```cpp
bool isConsecutivelyDescending(string s) {
	int n = s.size();
	if(n==1) return false;
	for(int len=1; len<=(n+1)/2; len++) {
		int num = stoi(s.substr(0, len)), i=0;
		while(i<n) {
			string snum = to_string(num);
			if(n-i<snum.size()) break;
			bool match = true;
			for(auto &ch:snum)
				if(s[i]==ch) ++i;
				else {match = false; break;}
			if(!match) break;
			--num;
		}
		if(i==n) return true;
	}
	return false;
}
```
