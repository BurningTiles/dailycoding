# Solution - 30 Aug 2023

---
## [1. Kth Largest in BST](https://workat.tech/problem-solving/practice/kth-largest-element-bst) 

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
		inorder(root->right, k, ans);
		if(!--k) { ans = root->data; return; }
		inorder(root->left, k, ans);
	}
}

int findKthLargest(Node* root, int k) {
	int ans = 0;
	inorder(root, k, ans);
	return ans;
}
```
