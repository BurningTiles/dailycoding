# Solution - 27 Feb 2024

---
## [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)

### cpp
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int traverse(TreeNode *root, int &ans) {
        if(!root) return 0;
        
        int left = traverse(root->left, ans), right = traverse(root->right, ans);
        ans = max(ans, left + right);
        
        return max(left, right) + 1;
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        traverse(root, ans);
        return ans;
    }
};
```
