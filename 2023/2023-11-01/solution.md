# Solution - 01 Nov 2023

---
## [501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree)

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
    int curr = 0, count = 0, max_count = 0;
    vector<int> v;
public:
    void traverse(TreeNode *root) {
        if(root) {
            traverse(root->left);
            if(root->val==curr) ++count;
            else curr = root->val, count = 1;
            
            if(count > max_count)
                max_count = count, v = {curr};
            else if(count == max_count)
                v.push_back(curr);

            traverse(root->right);
        }
    }

    vector<int> findMode(TreeNode* root) {
        curr = count = max_count = 0; v.clear();
        traverse(root);
        return v;
    }
};
```
