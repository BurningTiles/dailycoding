# Generate Brackets

### Python
```python
def generate_brackets(n):
	ans = []
	if n==0:
		return [""]
	for i in range(n):
		for left in generate_brackets(i):
			for right in generate_brackets(n-1-i):
				ans.append("(" + left + ")" + right)
	return ans
  
print(generate_brackets(1))
print(generate_brackets(3))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<string> generate_brackets(int n){
	vector<string> ans;
	if(n==0)
		return {""};
	for(int i=0; i<n; i++)
		for(string left: generate_brackets(i))
			for(string right: generate_brackets(n-1-i))
				ans.push_back("(" + left + ")" + right);
	return ans;
}

void print(vector<string> a) {
	if(!a.size()){
		cout << "Null" << endl; return;
	}

	cout << "[\'";
	for(int i=0; i<a.size(); i++)
		cout << a[i],
		cout << (i==a.size()-1 ? "\']" : "\', \'");
	cout << endl;
}

signed main() {
	print(generate_brackets(1));
	print(generate_brackets(3));
	return 0;
}
```

### Java
```java
import java.util.ArrayList;
import java.util.List;

public class solution {
	public static void main(String args[]) {
		System.out.println(generate_brackets(1));
		System.out.println(generate_brackets(3));
	}

	public static List<String> generate_brackets(int n) {
        List<String> ans = new ArrayList<String>();
        if (n == 0) {
            ans.add("");
        } else {
            for (int c = 0; c < n; ++c)
                for (String left: generate_brackets(c))
                    for (String right: generate_brackets(n-1-c))
                        ans.add("(" + left + ")" + right);
        }
        return ans;
    }
}
```

# [Referance](https://leetcode.com/problems/4sum/solution/)