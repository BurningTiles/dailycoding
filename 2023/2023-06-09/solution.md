# Solution - 09 Jun 2023

---
## [1. Search in a Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/search-in-a-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/search-in-a-binary-search-tree/) 

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

Node* searchBst(Node* root, int key) {
	if(!root) return NULL;
	if(root->data==key) return root;
	if(key<root->data) return searchBst(root->left, key);
	return searchBst(root->right, key);
}
```

---
## [2. Lowest Common Ancestor in BST](https://workat.tech/problem-solving/practice/lowest-common-ancestor-bst) [(LeetCode)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) 

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

Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {
	if(p->data < root->data && q->data < root->data)
		return lowestCommonAncestor(root->left, p, q);
	if(p->data > root->data && q->data > root->data)
		return lowestCommonAncestor(root->right, p, q);
	return root;
}
```