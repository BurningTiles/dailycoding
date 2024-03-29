# Solution - 05 Jun 2023

---
## [1. Binary Tree Postorder Traversal](https://workat.tech/problem-solving/practice/binary-tree-postorder-traversal) [(LeetCode)](https://leetcode.com/problems/binary-tree-postorder-traversal/) 

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

void postorder(Node *root, vector<int> &ans) {
	if(root) {
		postorder(root->left, ans);
		postorder(root->right, ans);
		ans.push_back(root->data);
	}
}

vector<int> getPostorderTraversal(Node* root) {
	vector<int> ans;
	postorder(root, ans);
	return ans;
}
```

---
## [2. Level Order of Binary Tree](https://workat.tech/problem-solving/practice/level-order-binary-tree) [(LeetCode)](https://leetcode.com/problems/binary-tree-level-order-traversal/) 

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

vector<int> getLevelOrderTraversal(Node* root) {
	if(!root) return {};
	vector<int> ans;
	queue<Node*> q;
	q.push(root);
	while(q.size()) {
		Node *tmp = q.front(); q.pop();
		ans.push_back(tmp->data);
		if(tmp->left) q.push(tmp->left);
		if(tmp->right) q.push(tmp->right);
	}
	return ans;
}
```