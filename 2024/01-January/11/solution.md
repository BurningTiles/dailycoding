# Solution - 11 Jan 2024

---
## [1026. Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor)

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
    int helper(TreeNode *root, int low, int high) {
        if(!root) return 0;

        low = min(low, root->val);
        high = max(high, root->val);

        int left = helper(root->left, low, high);
        int right = helper(root->right, low, high);
        
        return max(high-low, max(left, right));
    }

    int maxAncestorDiff(TreeNode* root) {
        return helper(root, INT_MAX, INT_MIN);
    }
};
```
### py
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], low, high):
        if root == None:
            return 0
        
        low = min([low, root.val])
        high = max([high, root.val])

        left = self.helper(root.left, low, high)
        right = self.helper(root.right, low, high)

        return max([high-low, left, right])

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 999999999, -999999999)
        
```
