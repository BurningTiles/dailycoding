# Solution - 28 Aug 2023

---
## [1. Delete Node in a Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/delete-node-from-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/delete-node-in-a-bst/) 

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

Node* removeFromBst(Node* root, int key) {
	if(root) {
		if(root->data > key)
			root->left = removeFromBst(root->left, key);
		else if(root->data < key)
			root->right = removeFromBst(root->right, key);
		else {
			if(!root->left) return root->right;
			if(!root->right) return root->left;
			
			Node *tmp = root->right;
			while(tmp->left) tmp = tmp->left;
			root->data = tmp->data;
			root->right = removeFromBst(root->right, tmp->data);
		}
	}
	return root;
}
```
