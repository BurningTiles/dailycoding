# Reverse Words in a String

### Python
```python
def reverseWords(s):
	ans = ""
	for s in s.split():
		ans += s[::-1]
		ans += " "
	return ans.rstrip()

print(reverseWords("The cat in the hat"))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string reverseWords(string s){
	string ans="";
	int j=-1, tmp;
	for(int i=0; i<s.size(); i++)
		if(s[i]==' '){
			tmp = i-1;
			while(tmp>j) ans += s[tmp--];
			ans += " ", j=i;
		}
	tmp = s.size()-1;
	while(tmp>j) ans += s[tmp--];
	return ans;
}

signed main() {
	cout << reverseWords("The cat in the hat") << endl;
	return 0;
}
```