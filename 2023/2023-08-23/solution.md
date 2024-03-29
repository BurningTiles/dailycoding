# Solution - 23 Aug 2023

---
## [1. Insert into a Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/insert-into-a-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/insert-into-a-binary-search-tree/) 

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

Node* insertBst(Node* root, int key) {
	if(!root) return new Node(key);
	if(key < root->data) 
		root->left = insertBst(root->left, key);
	else
		root->right = insertBst(root->right, key);
	return root;
}

/*
// Iterative approach
Node* insertBst(Node* root, int key) {
	if(!root) return new Node(key);
	Node *n = new Node(key), *tmp = root;
	while(true) {
		if(tmp->data > key && tmp->left)
			tmp = tmp->left;
		else if(tmp->data <= key && tmp->right)
			tmp = tmp->right;
		else break;
	}
	tmp->data > key ? tmp->left = n : tmp->right = n;
	return root;
}
*/
```
