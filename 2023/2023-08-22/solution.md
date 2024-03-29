# Solution - 22 Aug 2023

---
## [1. Populating Next Right Pointers in Each Node](https://workat.tech/problem-solving/practice/populating-next-right-pointers-in-each-node) [(LeetCode)](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) 

### cpp
```cpp
/* This is the Node class definition

class Node {
public:
	Node* left;
	Node* right;
	Node* next;
	int data;

	Node(int data) {
		this->left = NULL;
		this->right = NULL;
		this->next = NULL;
		this->data = data;
	}
};
*/

void connect(Node *root) {
	Node *prev = root, *curr;
	while(prev) {
		curr = prev;
		while(curr && curr->left) {
			curr->left->next = curr->right;
			if(curr->next) curr->right->next = curr->next->left;
			curr = curr->next;
		}
		prev = prev->left;
	}
}

/*
// If tree is not perfect binary tree
void connect(Node* root) {
	queue<Node*> q;
	q.push(root);
	while(q.size()) {
		int n = q.size();
		for(int i=1; i<=n; i++) {
			Node *tmp = q.front();
			q.pop();
			if(i!=n) tmp->next = q.front();
			if(tmp->left) q.push(tmp->left);
			if(tmp->right) q.push(tmp->right);
		}
	}
}
*/
```
