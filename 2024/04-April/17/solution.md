# Solution - 17 Apr 2024

---
## [988. Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf)

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
    string smallestFromLeaf(TreeNode* root, string ans = "") {
        if(root) {
            ans = char(root->val + 97) + ans;
            if(root->left || root->right)
                return min(smallestFromLeaf(root->left, ans),
                    smallestFromLeaf(root->right, ans));
            else
                return ans;
        }
        return "~";
    }
};
```
