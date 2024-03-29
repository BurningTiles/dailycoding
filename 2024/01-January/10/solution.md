# Solution - 10 Jan 2024

---
## [2385. Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected)

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
    int helper(TreeNode *root, int infected, int &ans) {
        if(!root) return 0;

        int depth = 0, left = helper(root->left, infected, ans), 
            right = helper(root->right, infected, ans);
        
        if(root->val == infected)
            ans = max(left, right), depth = -1;
        else if(left >= 0 && right >= 0)
            depth = max(left, right) + 1;
        else {
            int dist = abs(left) + abs(right);
            ans = max(ans, dist);
            depth = min(left, right) - 1;
        }

        return depth;
    }
    
    int amountOfTime(TreeNode* root, int start) {
        int ans = 0;
        helper(root, start, ans);
        return ans;
    }
};
```
