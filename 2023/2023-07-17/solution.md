# Solution - 17 Jul 2023

---
## [1. Next Greater Element](https://workat.tech/problem-solving/practice/next-greater-element) 

### cpp
```cpp
vector<int> getNextGreaterElement (vector<int> &A) {
	stack<int> stk;
	vector<int> ans(A.size());
	for(int i=A.size()-1; i>=0; i--) {
		while(!stk.empty() && stk.top()<=A[i]) stk.pop();
		if(stk.empty()) ans[i] = -1;
		else ans[i] = stk.top();
		stk.push(A[i]);
	}
	return ans;
}
```


---
## [2. Simplify Directory Path](https://workat.tech/problem-solving/practice/simplify-directory-path) [(LeetCode)](https://leetcode.com/problems/simplify-path/) 

### cpp
```cpp
string simplifyPath(string path) {
	path.push_back('/');
	stack<string> stk;
	string tmp = "";
	for(auto &ch:path) {
		if(ch=='/') {
			if(tmp=="..") {
				if(!stk.empty()) stk.pop();
			}
			else if(tmp != "." && tmp != "") stk.push(tmp);
			tmp = "";
		}
		else tmp.push_back(ch);
	}
	if(stk.empty()) tmp = "/";
	while(!stk.empty()) {
		tmp = "/" + stk.top() + tmp;
		stk.pop();
	}
	return tmp;
}
```
