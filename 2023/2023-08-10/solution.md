# Solution - 10 Aug 2023

---
## [1. Construct Binary Tree from Preorder and Inorder Traversal](https://workat.tech/problem-solving/practice/construct-binary-tree-from-preorder-and-inorder-traversal) [(LeetCode)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) 

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
unordered_map<int, int> um;

Node* generate(vector<int> &pre, int &i, int l, int r) {
	if(l>r) return NULL;
	int data = pre[i++];
	Node *ans = new Node(data);
	ans->left = generate(pre, i, l, um[data]-1);
	ans->right = generate(pre, i, um[data]+1, r);
	return ans;
}

Node* constructTree(vector<int> &preorder, vector<int> &inorder) {
	um.clear();
	for(int i=0; i<inorder.size(); i++) um[inorder[i]] = i;
	int i = 0;
	return generate(preorder, i, 0, preorder.size()-1);
}
```
