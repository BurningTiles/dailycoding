# Solution - 18 Aug 2023

---
## [1. Lowest Common Ancestor in Binary Tree](https://workat.tech/problem-solving/practice/lowest-common-ancestor) [(LeetCode)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) 

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

Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {
	Node *left=NULL, *right=NULL;
	if(root!=NULL) {
		left = lowestCommonAncestor(root->left, p, q);
		right = lowestCommonAncestor(root->right, p, q);
	}
	if(left && right) return root;
	if(root==p || root==q) return root;
	return left ? left : right;
}
```
