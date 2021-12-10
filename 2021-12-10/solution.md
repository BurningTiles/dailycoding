# Tree Serialization

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		# pre-order printing of the tree.
		result = ''
		result += str(self.value) + " "
		if self.left:
			result += str(self.left)
		if self.right:
			result += str(self.right)
		return result

def serialize(root):
	if root==None: return "# "
	return str(root.value) + " " + serialize(root.left) + serialize(root.right)

def deserialize_rec(s):
	if len(s)==0 or s[0]=='#':
		del s[0]
		return None
	n = Node(str(s[0]))
	del s[0]
	n.left = deserialize_rec(s)
	n.right = deserialize_rec(s)
	return n

def deserialize(s):
	return deserialize_rec(s.split())

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
n = Node(1, Node(3, Node(2), Node(5)), Node(4, None, Node(7)))

print(serialize(n))
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
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
	void print(){
		cout << value << " ";
		if(left) left->print(); if(right) right->print();
	};
};

string serialize(Node *n){
	if(!n) return "# ";
	return to_string(n->value) + " " + serialize(n->left) + serialize(n->right);
}
Node* deserialize_rec(string &s){
	if(!s.size() || s[0]=='#') {
		if(s.size()<2) s="";
		else s = s.substr(2);
		return NULL;
	}
	Node *n = new Node(stoi(s));
	s = s.substr(s.find(" ")+1);
	n->left = deserialize_rec(s);
	n->right = deserialize_rec(s);
	return n;
}

Node* deserialize(string s){
	return deserialize_rec(s);
}

signed main() {
	Node *n = new Node(1, new Node(3, new Node(2), new Node(5)), new Node(4, NULL, new Node(7)));

	cout << serialize(n) << endl;
	deserialize("1 3 2 # # 5 # # 4 # 7 # #")->print();

	return 0;
}
```