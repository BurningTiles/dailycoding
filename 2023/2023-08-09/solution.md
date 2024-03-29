# Solution - 09 Aug 2023

---
## [1. Binary Tree Zigzag Level Order Traversal](https://workat.tech/problem-solving/practice/zigzag-level-order-traversal) [(LeetCode)](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) 

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

vector<int> zigzagLevelOrderTraversal(Node* root) {
	if(!root) return {};
	deque<Node*> q = {root};
	vector<int> ans;
	bool rev = false;
	while(q.size()) {
		int n = q.size();
		for(int i=0; i<n; i++)
			if(rev) {
				Node* tmp = q.back(); q.pop_back();
				ans.push_back(tmp->data);
				if(tmp->right) q.push_front(tmp->right);
				if(tmp->left) q.push_front(tmp->left);
			} else {
				Node* tmp = q.front(); q.pop_front();
				ans.push_back(tmp->data);
				if(tmp->left) q.push_back(tmp->left);
				if(tmp->right) q.push_back(tmp->right);
			}
		rev = !rev;
	}
	return ans;
}
```
