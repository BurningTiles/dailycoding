# Solution - 01 Sep 2023

---
## [1. Binary Search Tree (BST) Iterator](https://workat.tech/problem-solving/practice/binary-search-tree-iterator) [(LeetCode)](https://leetcode.com/problems/binary-search-tree-iterator/) 

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

class BSTIterator {
	stack<Node*> stk;
	void addNodes(Node* root) {
		while(root) {
			stk.push(root);
			root = root->left;
		}
	}
	
public:
	BSTIterator(Node* root) {
		addNodes(root);
	}
	
	bool hasNext() {
		return stk.size();
	}
	
	Node* next() {
		if(stk.size()) {
			Node *tmp = stk.top(); stk.pop();
			addNodes(tmp->right);
			return tmp;
		}
		return NULL;
	}
};
```
