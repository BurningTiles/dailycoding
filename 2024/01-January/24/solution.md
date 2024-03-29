# Solution - 24 Jan 2024

---
## [1457. Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree)

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
    void traverse(TreeNode *root, int count[], int &ans) {
        if(root) {
            count[root->val]++;

            if(root->left) traverse(root->left, count, ans);
            if(root->right) traverse(root->right, count, ans);

            if(!root->left && !root->right) {
                int odd = 0, i = 10;
                while(i--) odd += count[i] & 1;
                if(odd < 2) ++ans;
            }

            count[root->val]--;
        }
    }

    int pseudoPalindromicPaths (TreeNode* root) {
        int count[10] = {0}, ans = 0;
        traverse(root, count, ans);
        return ans;
    }
};
```
