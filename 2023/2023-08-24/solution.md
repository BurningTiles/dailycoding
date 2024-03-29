# Solution - 24 Aug 2023

---
## [1. Inorder Successor of Node in BST](https://workat.tech/problem-solving/practice/inorder-successor-bst) 

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

Node* findSuccessor(Node* root, Node* p) {
	stack<Node*> stk;
	while(root && root != p) {
		stk.push(root);
		if(root->data > p->data)
			root = root->left;
		else
			root = root->right;
	}
	if(!root) return NULL;
	if(!root->right) {
		while(stk.size() && root->data > stk.top()->data)
			stk.pop();
		return stk.size() ? stk.top() : NULL;
	}
	root = root->right;
	while(root->left) root = root->left;
	return root;
}
```
