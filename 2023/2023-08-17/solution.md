# Solution - 17 Aug 2023

---
## [1. Bottom View of Binary Tree](https://workat.tech/problem-solving/practice/bottom-view-binary-tree) 

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

vector<int> bottomView(Node* root) {
	if(!root) return {};
	vector<int> left, right;
	queue<pair<Node *, int>> q;
	q.push({root, 0});
	while(q.size()) {
		Node *n = q.front().first;
		int pos = q.front().second;
		q.pop();
		if(pos>=0) {
			if(pos<right.size()) right[pos] = n->data;
			else right.push_back(n->data);
		} else {
			if(-1-pos<left.size()) left[-1-pos] = n->data;
			else left.push_back(n->data);
		}
		if(n->left) q.push({n->left, pos-1});
		if(n->right) q.push({n->right, pos+1});
	}
	reverse(left.begin(), left.end());
	left.insert(left.end(), right.begin(), right.end());
	return left;
}
```
