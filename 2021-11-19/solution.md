# String to Integer

### Python
```python
def convert_to_int(s):
	negative = False
	if s[0]=='-':
		negative = True
		s = s[1:]
	
	i, ans = 0, 0
	while i<len(s):
		if s[i]>='0' and s[i]<='9':
			ans = ans*10 + ord(s[i])-ord('0')
		else:
			break
		i += 1
	if i==len(s):
		return -ans if negative else ans
	return None

print(convert_to_int('-105') + 1)
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int convert_to_int(string s){
	bool negative=false;
	if(s[0]=='-')
		negative=true, 
		s = s.substr(1,s.size());
	
	int i=0, ans=0;
	for(; i<s.size(); i++)
		if(isdigit(s[i]))
			ans = ans*10 + s[i]-'0';
		else
			break;
	
	if(i==s.size())
		return (negative ? -ans : ans);

	cout << "Invalid number." << endl;
	return 0;
}

signed main() {
	cout << convert_to_int("-105")+1 << endl;
	return 0;
}
```