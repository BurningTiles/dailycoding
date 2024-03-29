# Solution - 08 Jun 2023

---
## [1. Invert Binary Tree](https://workat.tech/problem-solving/practice/invert-binary-tree) [(LeetCode)](https://leetcode.com/problems/invert-binary-tree/) 

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

void invertTree(Node* root) {
	if(root) {
		Node *tmp = root->left;
		root->left = root->right;
		root->right = tmp;
		invertTree(root->left);
		invertTree(root->right);
	}
}
```

---
## [2. Balanced Binary Tree](https://workat.tech/problem-solving/practice/balanced-binary-tree) [(LeetCode)](https://leetcode.com/problems/balanced-binary-tree/) 

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

int getDepth(Node *root, bool &ans) {
	if(root) {
		int left = getDepth(root->left, ans),
			right = getDepth(root->right, ans);
		if(abs(left-right)>1) ans = false;
		return max(left, right) + 1;
	}
	return 0;
}

bool isBinaryTreeBalanced(Node* root) {
	bool ans = true;
	getDepth(root, ans);
	return ans;
}
```