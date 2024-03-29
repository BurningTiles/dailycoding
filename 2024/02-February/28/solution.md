# Solution - 28 Feb 2024

---
## [513. Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value)

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
    void traverse(TreeNode *root, int curDepth, int &depth, int &ans) {
        if(!root) return;
        
        traverse(root->left, curDepth+1, depth, ans);
        if(curDepth > depth) depth = curDepth, ans = root->val;
        traverse(root->right, curDepth+1, depth, ans);
    }

    int findBottomLeftValue(TreeNode* root) {
        int curDepth=0, depth=-1, ans=0;
        traverse(root, curDepth, depth, ans);
        return ans;
    }
};
```
