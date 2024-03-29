# Solution - 12 Jun 2023

---
## [1. Two Sum in BST](https://workat.tech/problem-solving/practice/two-sum-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) 

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

void inorder(Node *root, vector<int> &nums) {
	if(root) {
		inorder(root->left, nums);
		nums.push_back(root->data);
		inorder(root->right, nums);
	}
}

bool pairExists(Node* root, int k) {
	vector<int> nums;
	inorder(root, nums);
	int i=0, j=nums.size()-1, sum;
	while(i<j) {
		sum = nums[i] + nums[j];
		if(sum==k) return true;
		sum<k ? ++i : --j;
	}
	return false;
}
```

---
## [2. Excel Column Number](https://workat.tech/problem-solving/practice/excel-column) [(LeetCode)](https://leetcode.com/problems/excel-sheet-column-number/) 

```cpp
int getColumnNumber(string excelColumnNumber) {
	int ans = 0;
	for(auto ch: excelColumnNumber)
		ans = ans * 26 + ch - 64;
	return ans;
}
```