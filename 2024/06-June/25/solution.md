# Solution - 25 Jun 2024

---
## [1038. Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree)

### cpp
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int dfs(TreeNode *root, int sum = 0) {
        if(root) {
            int right = dfs(root->right, sum);
            root->val += right;
            return dfs(root->left, root->val);
        }
        return sum;
    }

    TreeNode* bstToGst(TreeNode* root) {
        dfs(root);
        return root;
    }
};
```
