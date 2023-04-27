# Longest Substring Without Repeating Characters

### Python
```python
def lengthOfLongestSubstring(s):
	count = dict()
	j, ans, curLen = 0, 0, 0
	for i in range(len(s)):
		if s[i] not in count:
			count[s[i]] = 1
			curLen += 1
		else:
			while s[i] in count:
				del count[s[j]]
				curLen -= 1
				j += 1
			count[s[i]] = 1
			curLen += 1
		ans = max([ans, curLen])
	return ans

print(lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLongestSubstring(string s){
	int count[128] = {0};
	int j=0, len=0, curLen=0;
	for(int i=0; i<s.size(); i++){
		if(!count[s[i]])
			count[s[i]]++,
			curLen++;
		else{
			while(count[s[i]]){
				count[s[j]]--;
				curLen--;
				j++;
			}
			count[s[i]] = 1;
			curLen++;
		}
		len = max(len, curLen);
	}
	return len;
}

signed main() {
	cout << lengthOfLongestSubstring("abrkaabcdefghijjxxx") << endl;
	return 0;
}
```