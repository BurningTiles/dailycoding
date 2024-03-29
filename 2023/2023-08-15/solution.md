# Solution - 15 Aug 2023

---
## [1. Right View of Binary Tree](https://workat.tech/problem-solving/practice/right-view-binary-tree) [(LeetCode)](https://leetcode.com/problems/binary-tree-right-side-view/) 

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

void rightView(Node *root, vector<int> &ans, int &maxDepth, int curDepth) {
	if(root) {
		if(curDepth > maxDepth) {
			ans.push_back(root->data);
			maxDepth = curDepth;
		}
		rightView(root->right, ans, maxDepth, curDepth + 1);
		rightView(root->left, ans, maxDepth, curDepth + 1);
	}
}

vector<int> rightView(Node* root) {
	vector<int> ans;
	int maxDepth = -1;
	rightView(root, ans, maxDepth, 0);
	return ans;
}
```
