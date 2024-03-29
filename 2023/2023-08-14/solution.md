# Solution - 14 Aug 2023

---
## [1. Left View of Binary Tree](https://workat.tech/problem-solving/practice/left-view-binary-tree) 

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

void leftView(Node *root, vector<int> &ans, int &maxDepth, int curDepth) {
	if(root) {
		if(curDepth > maxDepth) {
			ans.push_back(root->data);
			maxDepth = curDepth;
		}
		leftView(root->left, ans, maxDepth, curDepth + 1);
		leftView(root->right, ans, maxDepth, curDepth + 1);
	}
}

vector<int> leftView(Node* root) {
	vector<int> ans;
	int maxDepth = -1;
	leftView(root, ans, maxDepth, 0);
	return ans;
}
```
