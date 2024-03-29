# Solution - 25 Aug 2023

---
## [1. Inorder Predecessor of Node in BST](https://workat.tech/problem-solving/practice/inorder-predecessor-bst) 

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

Node* findPredecessor(Node* root, Node* p) {
	stack<Node*> stk;
	while(root && root != p) {
		stk.push(root);
		if(root->data > p->data)
			root = root->left;
		else
			root = root->right;
	}
	if(!root) return NULL;
	if(!root->left) {
		while(stk.size() && root->data < stk.top()->data)
			stk.pop();
		return stk.size() ? stk.top() : NULL;
	}
	root = root->left;
	while(root->right) root = root->right;
	return root;
}
```
