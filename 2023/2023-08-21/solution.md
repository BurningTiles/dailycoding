# Solution - 21 Aug 2023

---
## [1. Flatten Binary Tree to Linked List](https://workat.tech/problem-solving/practice/flatten-binary-tree-to-linked-list) [(LeetCode)](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) 

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

Node* flatten(Node* root) {
	if(root) {
		Node *leftLast = flatten(root->left);
		Node *rightLast = flatten(root->right);
		if(leftLast) {
			leftLast->right = root->right;
			root->right = root->left;
			root->left = NULL;
		}
		if(rightLast) return rightLast;
		if(leftLast) return leftLast;
		return root;
	}
	return NULL;
}
```
