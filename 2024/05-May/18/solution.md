# Solution - 18 May 2024

---
## [979. Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree)

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
    int distributeCoins(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        return ans;
    }

    int dfs(TreeNode* root, int &ans) {
        if(root) {
            int left = dfs(root->left, ans);
            int right = dfs(root->right, ans);
            ans += abs(left) + abs(right);
            return root->val + left + right - 1;
        }
        return 0;
    }
};
```
