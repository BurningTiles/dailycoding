# Remove One Layer of Parenthesis

### Python
```python
def remove_outermost_parenthesis(s):
	ans, op = "", 0
	for ch in s:
		if ch=='(':
			if op: ans+=ch
			op += 1
		else:
			op -= 1
			if op: ans+=ch
	return ans

print(remove_outermost_parenthesis("(())()"))
print(remove_outermost_parenthesis("(()())"))
print(remove_outermost_parenthesis("()()()"))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string remove_outermost_parenthesis(string s){
	string ans="";
	for(int i=0, open=0; i<s.size(); i++){
		if(s[i]=='('){
			if(open) ans+=s[i];
			++open;
		}
		else{
			--open;
			if(open) ans+=s[i];
		}
	}
	return ans;
}

signed main() {
	cout << remove_outermost_parenthesis("(())()") << endl;
	cout << remove_outermost_parenthesis("(()())") << endl;
	cout << remove_outermost_parenthesis("()()()") << endl;
	return 0;
}
```