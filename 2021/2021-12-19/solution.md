# Decode String

### Python
```python
def decodeString(s):
	i, ans = 0, ""
	while i<len(s):
		if s[i]>='0' and s[i]<='9':
			j=i+1
			while j<len(s) and s[j]!='[': j+=1
			rep, openBrackets = int(s[i:j]), 1
			j += 1
			i = j
			while openBrackets>0:
				if s[j]=='[': openBrackets+=1
				elif s[j]==']': openBrackets-=1
				j += 1
			reps = decodeString(s[i:j-1])
			while rep>0:
				ans += reps
				rep -= 1
			i = j
		else:
			ans += s[i]
			i += 1
	return ans

print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
print(decodeString("abc3[cd]xyz"))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string decodeString(string s){
	int i=0;
	string ans = "";
	while(i<s.size()){
		if(isdigit(s[i])){
			int j=i+1;
			while(j<s.size() && s[j]!='[') j++;
			int rep = stoi(s.substr(i, j-i)), open=1;
			i = ++j;
			while(open){
				if(s[j]=='[') ++open;
				else if(s[j]==']') --open;
				j++;
			}
			string reps = decodeString(s.substr(i, j-i-1));
			while(rep--) ans += reps;
			i=j;
		}
		else ans.push_back(s[i++]);
	}
	return ans;
}

signed main() {
	cout << decodeString("3[a]2[bc]") << endl;
	cout << decodeString("3[a2[c]]") << endl;
	cout << decodeString("2[abc]3[cd]ef") << endl;
	cout << decodeString("abc3[cd]xyz") << endl;
	return 0;
}
```