# Sum Binary Numbers

### Python
```python
def sum_binary(n1, n2):
	ans = ""
	i,j,s = len(n1)-1, len(n2)-1, 0
	while i>=0 or j>=0 or s>0:
		s += int(n1[i]) if i>=0 else 0
		s += int(n2[j]) if j>=0 else 0
		ans += str(s%2)
		i -= 1
		j -= 1
		s = s//2
	return ans[::-1]
	
print(sum_binary("11101", "1011"))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

string sum_binary(string n1, string n2) {
	string ans="";
	int i=n1.size()-1, j=n2.size()-1, sum=0;
	while(i>=0 || j>=0 || sum>0)
		sum += i>=0 ? n1[i]-'0' : 0, 
		sum += j>=0 ? n2[j]-'0' : 0, 
		ans.push_back(sum%2+'0'), 
		sum /= 2, --i, --j;
	reverse(ans.begin(), ans.end());
	return ans;
}

signed main() {
	cout << sum_binary("11101", "1011");
	
	return 0;
}
```

### Java
```java
public class solution {
	public static void main(String args[]) {
		System.out.println(sum_binary("11101", "1011"));
	}

	public static String sum_binary(String n1, String n2) {
		String ans = "";
		int i=n1.length()-1, j=n2.length()-1, sum=0;
		while(i>=0 || j>=0 || sum>0){
			sum += i>=0 ? n1.charAt(i)-'0' : 0;
			sum += j>=0 ? n2.charAt(j)-'0' : 0;
			ans = (char)(sum%2+'0') + ans;
			sum /= 2;
			--i;
			--j;
		}
		return ans;
	}
}
```