# Ransom Note

### Python
```python
def canSpell(magazine, note):
	a = [0]*26
	for ch in magazine:
		a[ord(ch)-97] += 1
	for ch in note:
		if a[ord(ch)-97]==0:
			return False
		a[ord(ch)-97] -= 1
	return True

print(canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
print(canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "True" : "False")
using namespace std;

bool canSpell(vector<char> magazine, string note) {
	int a[26] = {0};
	for(auto ch:magazine)
		a[ch-97]++;
	for(auto ch:note){
		if(!a[ch-97]) return false;
		a[ch-97]--;
	}
	return true;
}

signed main() {
	bool ans = canSpell({'a', 'b', 'c', 'd', 'e', 'f'}, "bed");
	cout << toBool(ans) << endl;
	ans = canSpell({'a', 'b', 'c', 'd', 'e', 'f'}, "cat");
	cout << toBool(ans) << endl;
	return 0;
}
```