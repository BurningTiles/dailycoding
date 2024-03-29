# Solution - 07 Jun 2023

---
## [1. Maximum Depth of Binary Tree](https://workat.tech/problem-solving/practice/maximum-depth-of-binary-tree) [(LeetCode)](https://leetcode.com/problems/maximum-depth-of-binary-tree/) 

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

int getMaxDepth(Node* root) {
	if(root)
		return 1 + max(getMaxDepth(root->left), getMaxDepth(root->right));
	return 0;
}
```

---
## [2. Diameter of Binary Tree](https://workat.tech/problem-solving/practice/diameter-of-binary-tree) [(LeetCode)](https://leetcode.com/problems/diameter-of-binary-tree/) 

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

int getDiameter(Node *root, int &ans) {
	if(!root) return 0;
	int left = getDiameter(root->left, ans),
		right = getDiameter(root->right, ans);
	ans = max(ans, left+right);
	return 1 + max(left, right);
}

int getDiameter(Node* root) {
	int ans = 0;
	getDiameter(root, ans);
	return ans;
}
```