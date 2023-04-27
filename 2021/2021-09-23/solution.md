# Remove Adjacent Duplicate Characters

### CPP
```cpp
/**
 * Author  : BurningTiles
 * Created : 2021-09-23 21:57:17
 * Link    : BurningTiles.github.io
 * File    : solution.cpp
**/

#include <bits/stdc++.h>
using namespace std;

bool remove_adjacent_duplicate(string &s){
	for(int i=1; i<s.size(); i++)
		if(s[i]==s[i-1]){
			s = s.substr(0,i-1) + s.substr(i+1,s.size());
			return true;
		}
	return false;
}

signed main() {
	string s;
	cin >> s;
	while(remove_adjacent_duplicate(s));
	cout << s;
	return 0;
}
```