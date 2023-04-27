# Unique Binary Search Trees II

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		# pre-order printing of the tree.
		i, q, ans = 0, [self], []
		while i<len(q):
			tmp = q[i]
			i += 1
			if tmp==None:
				ans.append(None)
				continue
			ans.append(tmp.value)
			if tmp.left==None and tmp.right==None: continue
			q.append(tmp.left)
			q.append(tmp.right)
		if not ans[-1]: del ans[-1]
		return str(ans)

def generateTrees(e, s=1):
	if s>e: return [None]
	ans = []
	for i in range(s, e+1):
		left = generateTrees(i-1, s)
		right = generateTrees(e, i+1)
		for l in left:
			for r in right:
				ans.append(Node(i, l, r))
	return ans

v = generateTrees(3)
for n in v:
	print(n)
```

### C++
```cpp
#include <bits/stdc++.h>
#define i2d vector<vector<int>>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

vector<Node*> generateTrees(int e, int s=1) {
	if(s>e) return {NULL};
	vector<Node*> ans;
	for(int i=s; i<=e; i++){
		vector<Node*> left = generateTrees(i-1, s);
		vector<Node*> right = generateTrees(e, i+1);
		for(auto &l:left)
			for(auto &r:right)
				ans.push_back(new Node(i, l, r));
	}
	return ans;
}

string get(Node *n){
	deque<Node*> dq;
	dq.push_back(n);
	string ans = "[";
	while(dq.size()){
		Node *tmp = dq.front();
		dq.pop_front();
		if(!tmp){
			ans += "NULL, ";
			continue;
		}
		ans += to_string(tmp->value) + ", ";
		if(!tmp->left && !tmp->right) continue;
		dq.push_back(tmp->left);
		dq.push_back(tmp->right);
	}
	if(ans.size()>1) {
		ans = ans.substr(0, ans.size()-2);
		if(ans.back()=='L') ans = ans.substr(0, ans.size()-6);
	}
	ans += "]";
	return ans;
}

signed main() {
	vector<Node*> v = generateTrees(3);
	for(auto n:v)
		cout << get(n) << endl;

	return 0;
}
```