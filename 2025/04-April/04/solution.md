# Solution - 04 Apr 2025

---
## [1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves)

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
    pair<TreeNode*, int> traverse(TreeNode *root) {
        if(root) {
            auto left = traverse(root->left);
            auto right = traverse(root->right);

            if(left.second > right.second)
                return {left.first, left.second + 1};
            if(left.second < right.second)
                return {right.first, right.second + 1};
            return {root, left.second + 1};
        }
        return {NULL, 0};
    }

    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return traverse(root).first;
    }
};
```
