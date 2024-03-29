# Solution - 06 Jun 2023

---
## [1. Identical Binary Trees](https://workat.tech/problem-solving/practice/identical-binary-trees) [(LeetCode)](https://leetcode.com/problems/same-tree/) 

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

bool areIdenticalTrees(Node* root1, Node* root2) {
	if(root1 && root2 && root1->data==root2->data)
		return areIdenticalTrees(root1->left, root2->left) && 
			areIdenticalTrees(root1->right, root2->right);
	else if(!root1 && !root2) return true;
	return false;
}
```

---
## [2. Symmetric Binary Tree](https://workat.tech/problem-solving/practice/symmetric-binary-tree) [(LeetCode)](https://leetcode.com/problems/symmetric-tree/) 

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
bool isMirror(Node *n1, Node *n2) {
	if(n1 && n2 && n1->data==n2->data)
		return isMirror(n1->left, n2->right) && 
			isMirror(n1->right, n2->left);
	return !(n1 || n2);
}

bool isSymmetric(Node* root) {
	return isMirror(root, root);
}
```