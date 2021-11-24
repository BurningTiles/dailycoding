# Validate Balanced Parentheses

### Python
```python
def isValid(s):
	stk = []
	for c in s:
		if c=='(' or c=='[' or c=='{':
			stk.append(c)
		else:
			if len(stk)==0:
				return False
			elif c==']' and stk[-1]=='[': pass
			elif c==')' and stk[-1]=='(': pass
			elif c=='}' and stk[-1]=='{': pass
			else: return False
			del stk[-1]
	return len(stk)==0

print(isValid("()(){(())"))
print(isValid(""))
print(isValid("([{}])()"))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool isValid(string s){
	stack<char> stk;
	char c;
	for(int i=0; i<s.size(); i++){
		c = s[i];
		if(c=='(' || c=='[' || c=='{')
			stk.push(c);
		else {
			if(!stk.size()) return false;
			else if(c==']' && stk.top()=='[');
			else if(c==')' && stk.top()=='(');
			else if(c=='}' && stk.top()=='{');
			else return false;
			stk.pop();
		}
	}
	return stk.size()==0;
}

signed main() {
	cout << toBool(isValid("()(){(())")) << endl;
	cout << toBool(isValid("")) << endl;
	cout << toBool(isValid("([{}])()")) << endl;
	return 0;
}
```