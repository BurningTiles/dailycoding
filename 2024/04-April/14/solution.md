# Solution - 14 Apr 2024

---
## [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves)

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
    int sumOfLeftLeaves(TreeNode* root, bool left=false) {
        if(root) {
            if(!root->left && !root->right && left)
                return root->val;
            return (root->left ? sumOfLeftLeaves(root->left, true) : 0) + 
                (root->right ? sumOfLeftLeaves(root->right) : 0);
        }
        return 0;
    }
};
```
