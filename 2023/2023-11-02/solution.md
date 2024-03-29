# Solution - 02 Nov 2023

---
## [2265. Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree)

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
    pair<int, int> traverse(TreeNode *root, int &ans) {
        if(root) {
            pair<int, int> left = traverse(root->left, ans), right = traverse(root->right, ans);
            int total = root->val + left.first + right.first, 
                size = 1 + left.second + right.second;
            if(int(double(total) / size)==root->val) ++ans;
            return {total, size};
        }
        return {0, 0};
    }

    int averageOfSubtree(TreeNode* root) {
        int ans = 0;
        traverse(root, ans);
        return ans;
    }
};
```
