# Solution - 11 Aug 2023

---
## [1. Construct Binary Tree from Inorder and Postorder Traversal](https://workat.tech/problem-solving/practice/construct-binary-tree-from-inorder-and-postorder-traversal) [(LeetCode)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) 

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

Node* generate(vector<int> &post, int &i, int l, int r) {
	if(l>r) return NULL;
	int data = post[i--];
	Node *ans = new Node(data);
	ans->right = generate(post, i, um[data]+1, r);
	ans->left = generate(post, i, l, um[data]-1);
	return ans;
}

Node* constructTree(vector<int> &postorder, vector<int> &inorder) {
	um.clear();
	for(int i=0; i<inorder.size(); i++) um[inorder[i]] = i;
	int i = inorder.size()-1;
	return generate(postorder, i, 0, inorder.size()-1);
}
```
