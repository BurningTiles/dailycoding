# Common Characters

### CPP
```cpp
/**
 * Author  : BurningTiles
 * Created : 2021-09-25 02:07:34
 * Link    : BurningTiles.github.io
 * File    : solution.cpp
**/

#include <bits/stdc++.h>
using namespace std;

vector<char> common_characters(vector<string> v) {
	vector<char> ans;
	vector<bool> flag(26,true);
	for(int i=0; i<v.size(); i++){
		vector<bool> flagStr(26, false);
		for(int j=0; j<v[i].size(); j++)
			if(flag[v[i][j]-97])
				flagStr[v[i][j]-97] = true;
		flag = flagStr;
	}
	for(int i=0; i<26; i++)
		if(flag[i])
			ans.push_back(i+97);
	return ans;
}

signed main() {

	// input
	int n;
	cin >> n;
	vector<string> v(n);
	for(int i=0; i<n; i++)
		cin >> v[i];

	// calling function
	vector<char> ans = common_characters(v);
	n = ans.size();

	// printing output.
	cout << '[';
	for(int i=0; i<n-1; i++)
		cout << '\'' << ans[i] << "\', ";
	if(n)
		cout << '\'' << ans.back() << "\']" << endl;
	else
		cout << "]" << endl;
	
	return 0;
}
```

### Python
```python
#
# Author  : BurningTiles
# Created : 2021-09-25 02:57:25
# Link    : BurningTiles.github.io
#

def common_characters(a):
	ans = []
	flag = [True]*26
	for i in range(len(a)):
		flagStr = [False]*26
		for j in range(len(a[i])):
			if flag[ord(a[i][j])-97]:
				flagStr[ord(a[i][j])-97] = True
		flag = flagStr
	for i in range(26):
		if flag[i]:
			ans.append(chr(i+97))
	return ans

n = int(input())
a = []
for i in range(n):
	a.append(input())
print(common_characters(a))
```

# Old

### CPP
```cpp
/**
 * Author  : BurningTiles
 * Created : 2021-09-25 02:07:34
 * Link    : BurningTiles.github.io
 * File    : solution.cpp
**/

#include <bits/stdc++.h>
using namespace std;

vector<char> common_characters(vector<string> v) {
	vector<char> ans;
	bool flag[v.size()][26]={false};
	for(int i=0; i<v.size(); i++){
		for(int j=0; j<v[i].size(); j++)
			flag[i][v[i][j]-97] = 1;
	}
	for(int i=0; i<26; i++){
		bool ch = true;
		for(int j=0; j<v.size(); j++)
			if(!flag[j][i]){
				ch = false;
				break;
			}
		if(ch) ans.push_back(i+97);
	}
	return ans;
}

signed main() {

	// input
	int n;
	cin >> n;
	vector<string> v(n);
	for(int i=0; i<n; i++)
		cin >> v[i];

	// calling function
	vector<char> ans = common_characters(v);
	n = ans.size();

	// printing output.
	cout << '[';
	for(int i=0; i<n-1; i++)
		cout << '\'' << ans[i] << "\', ";
	if(n)
		cout << '\'' << ans.back() << "\']" << endl;
	else
		cout << "]" << endl;
	
	return 0;
}
```

### Python
```python
#
# Author  : BurningTiles
# Created : 2021-09-25 02:57:25
# Link    : BurningTiles.github.io
#

def common_characters(a):
	ans = []
	flag = [[False]*26 for _ in range(len(a))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			flag[i][ord(a[i][j])-97] = True
	for i in range(26):
		ch = True
		for j in range(len(a)):
			if not flag[j][i]:
				ch = False
				break
		if ch:
			ans.append(chr(i+97))
	return ans

n = int(input())
a = []
for i in range(n):
	a.append(input())
print(common_characters(a))
```