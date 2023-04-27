# Generate Brackets

### Python
```python
def generate_brackets(n):
	ans = []
	def backtrack(s = [], left = 0, right = 0):
		if len(s) == 2 * n:
			ans.append("".join(s))
			return
		if left < n:
			s.append("(")
			backtrack(s, left+1, right)
			s.pop()
		if right < left:
			s.append(")")
			backtrack(s, left, right+1)
			s.pop()
	backtrack()
	return ans

print(generate_brackets(1))
print(generate_brackets(3))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<string> &ans, string cur, int open, int close, int max) {
	if(cur.size()==max*2){
		ans.push_back(cur);
		return;
	}
	if(open<max)
		cur.push_back('('),
		backtrack(ans, cur, open+1, close, max),
		cur.pop_back();
	if(close<open)
		cur.push_back(')'),
		backtrack(ans, cur, open, close+1, max),
		cur.pop_back();
}

vector<string> generate_brackets(int n){
	vector<string> ans;
	backtrack(ans, "", 0, 0, n);
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
		backtrack(ans, new StringBuilder(), 0, 0, n);
		return ans;
	}
	
	public static void backtrack(List<String> ans, StringBuilder cur, int open, int close, int max){
		if (cur.length() == max * 2) {
			ans.add(cur.toString());
			return;
		}
		if (open < max) {
			cur.append("(");
			backtrack(ans, cur, open+1, close, max);
			cur.deleteCharAt(cur.length() - 1);
		}
		if (close < open) {
			cur.append(")");
			backtrack(ans, cur, open, close+1, max);
			cur.deleteCharAt(cur.length() - 1);
		}
	}
}
```

# OLD

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