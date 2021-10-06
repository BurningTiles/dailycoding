# Longest Common Prefix

### Python
```python
def longest_common_prefix(s):
	if len(s)==0:
		return ""
	prefix = s[0]
	for i in range(1,len(s)):
		j=0
		while j<len(s[i]) and j<len(prefix) and s[i][j]==prefix[j]:
			j += 1
		if j==0:
			return ""
		prefix = prefix[:j]
	return prefix

print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
print(longest_common_prefix(['daily', 'interview', 'pro']))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

string longest_common_prefix(vector<string> v){
	if (v.size() == 0) return "";
    string prefix = v[0];
    for (int i=1; i<v.size(); i++){
		int j=0;
		while(j<v[i].size() && j<prefix.size() && v[i][j]==prefix[j]) j++;
		if(j==0) return "";
		prefix = prefix.substr(0,j);
	}    
    return prefix;
}

signed main() {
	cout << longest_common_prefix({"helloworld", "hellokitty", "hell"}) << endl;
	cout << longest_common_prefix({"daily", "interview", "pro"}) << endl;
	return 0;
}
```

### Java
```java
public class solution {
	public static void main(String args[]) {
		String s1[] = {"helloworld", "hellokitty", "hell"};
		String s2[] = {"daily", "interview", "pro"};
		System.out.println(longest_common_prefix(s1));
		System.out.println(longest_common_prefix(s2));
	}

	public static String longest_common_prefix(String s[]) {
		if(s.length==0) return "";
		String prefix = s[0];
		for(int i=1; i<s.length; i++){
			int j=0;
			while(j<s[i].length() && j<prefix.length() && s[i].charAt(j)==prefix.charAt(j))
				j++;
			if(j==0) return "";
			prefix = prefix.substring(0, j);
		}
		return prefix;
	}
}
```