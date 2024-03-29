# Solution - 08 Dec 2023

---
## [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree)

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
    void inorder(TreeNode* root, string &ans) {
        if(root) {
            ans += to_string(root->val);
            if(!root->left && !root->right) return;

            ans.push_back('(');
            inorder(root->left, ans);
            ans.push_back(')');

            if(root->right) {
                ans.push_back('(');
                inorder(root->right, ans);
                ans.push_back(')');
            }
        }
    }

    string tree2str(TreeNode* root) {
        string ans = "";
        inorder(root, ans);
        return ans;
    }
};
```
