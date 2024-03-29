# Solution - 16 Aug 2023

---
## [1. Top View of Binary Tree](https://workat.tech/problem-solving/practice/top-view-binary-tree) 

### cpp
```cpp
/* This is the Node class definition

class Node {
public:
	Node* left;
	Node* right;
	int data;

	Node(int data) {
		this->left = NULL;
		this->right = NULL;
		this->data = data;
	}
};
*/

vector<int> topView(Node* root) {
	if(!root) return {};
	vector<int> left, right;
	queue<pair<Node *, int>> q;
	q.push({root, 0});
	while(q.size()) {
		Node *n = q.front().first;
		int pos = q.front().second;
		q.pop();
		if(pos>=0) {
			if(pos==right.size()) right.push_back(n->data);
		} else {
			if(-pos>left.size()) left.push_back(n->data);
		}
		if(n->left) q.push({n->left, pos-1});
		if(n->right) q.push({n->right, pos+1});
	}
	reverse(left.begin(), left.end());
	left.insert(left.end(), right.begin(), right.end());
	return left;
}
```
