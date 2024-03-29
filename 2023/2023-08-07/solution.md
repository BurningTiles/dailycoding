# Solution - 07 Aug 2023

---
## [1. Restore IP Addresses](https://workat.tech/problem-solving/practice/restore-ip-addresses) [(LeetCode)](https://leetcode.com/problems/restore-ip-addresses/) 

### cpp
```cpp
bool isValid(string s, int i, int j) {
	int len = j-i;
	if(len>3 || len<1 || (len>1 && s[i]=='0')) return false;
	if(len==3) return s.substr(i, 3) <= "255";
	return true;
}

vector<string> restoreIPAddresses(string s) {
	vector<string> ans;
	int n = s.size();
	if(n<3 || n>12) return {};
	for(int i=1; i<=3 && i<n; i++) {
		if(!isValid(s, 0, i)) continue;
		for(int j=i+1; j<i+4 && j<n; j++) {
			if(!isValid(s, i, j)) continue;
			for(int k=j+1; k<j+4 && k<n; k++) {
				if(!isValid(s, j, k)) continue;
				if(isValid(s, k, s.size())) {
					// cout << i << " " << j << " " << k << endl;
					ans.push_back(s.substr(0, i  ) + "." + 
								  s.substr(i, j-i) + "." +
								  s.substr(j, k-j) + "." +
								  s.substr(k, n  ));
				}
			}
		}
	}
	return ans;
}
```
