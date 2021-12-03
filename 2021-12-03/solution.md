# No Adjacent Repeating Characters

### Python
```python
def rearrangeString(s):
	count = [0]*26
	for ch in s:
		count[ord(ch)-97] += 1
	chars = []
	for i in range(26):
		if count[i]>0:
			chars.append([i, count[i]])
	chars.sort(reverse=True, key=lambda x: x[1])
	tmp, ans = 0, ""
	for x in chars:
		ch = chr(x[0]+97)
		while x[1]>0:
			x[1] -= 1
			if tmp<0:
				tmp = len(ans)-1
			ans = ans[:tmp] + ch + ans[tmp:]
			tmp -= 1
	for i in range(1, len(ans)):
		if ans[i]==ans[i-1]: return "Not Possible"
	return ans

print(rearrangeString("abbccc"))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> &a, pair<int, int> &b){
	return a.second<b.second;
}

string rearrangeString(string s){
	int count[26]={0};
	for(int i=0; i<s.size(); i++)
		count[s[i]-97]++;
	vector<pair<int, int>> v;
	for(int i=0; i<26; i++)
		if(count[i]) v.push_back({i, count[i]});
	sort(v.rbegin(), v.rend(), cmp);
	int tmp=0;
	string ans="";
	for(auto x:v){
		char ch=x.first+97;
		while(x.second--){
			if(tmp<0) tmp = ans.size()-1;
			ans.insert(ans.begin()+tmp, ch);
			tmp--;
		}
	}
	for(int i=1; i<ans.size(); i++)
		if(ans[i]==ans[i-1]) return "Not Possible";
	return ans;
}

signed main() {
	cout << rearrangeString("abbccc") << endl; 
	return 0;
}
```