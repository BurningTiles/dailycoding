# Solution - 31 Aug 2023

---
## [1. Kth Smallest in BST](https://workat.tech/problem-solving/practice/kth-smallest-element-bst) [(LeetCode)](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) 

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

void inorder(Node *root, int &k, int &ans) {
	if(root) {
		inorder(root->left, k, ans);
		if(!--k) { ans = root->data; return; }
		inorder(root->right, k, ans);
	}
}

int findKthSmallest(Node* root, int k) {
	int ans = 0;
	inorder(root, k, ans);
	return ans;
}
```
