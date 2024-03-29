# Solution - 02 Jun 2023

---
## [1. Binary Tree Inorder Traversal](https://workat.tech/problem-solving/practice/binary-tree-inorder-traversal) [(LeetCode)](https://leetcode.com/problems/binary-tree-inorder-traversal/) 

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

void inorder(Node *root, vector<int> &ans) {
	if(root) {
		inorder(root->left, ans);
		ans.push_back(root->data);
		inorder(root->right, ans);
	}
}

vector<int> getInorderTraversal(Node *root) {
	vector<int> ans;
	inorder(root, ans);
	return ans;
}
```

---
## [2. Binary Tree Preorder Traversal](https://workat.tech/problem-solving/practice/binary-tree-preorder-traversal) [(LeetCode)](https://leetcode.com/problems/binary-tree-preorder-traversal/) 

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

void preorder(Node *root, vector<int> &ans) {
	if(root) {
		ans.push_back(root->data);
		preorder(root->left, ans);
		preorder(root->right, ans);
	}
}

vector<int> getPreorderTraversal(Node* root) {
	vector<int> ans;
	preorder(root, ans);
	return ans;
}
```