# Solution - 29 Aug 2023

---
## [1. Is Binary Tree BST](https://workat.tech/problem-solving/practice/is-binary-tree-bst) [(LeetCode)](https://leetcode.com/problems/validate-binary-search-tree/) 

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

bool isBst(Node* root, long left=LONG_MIN, long right=LONG_MAX) {
	if(root) {
		if(root->data < left || root->data > right) return false;
		return isBst(root->left, left, root->data - 1L) && 
			isBst(root->right, root->data + 1L, right);
	}
	return true;
}
```
