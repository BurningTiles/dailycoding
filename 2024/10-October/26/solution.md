# Solution - 26 Oct 2024

---
## [2458. Height of Binary Tree After Subtree Removal Queries](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries)

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
    int seen[100001], maxh;
public:
    void dfs(TreeNode *root, int h) {
        if(!root) return;
        seen[root->val] = max(seen[root->val], maxh);
        maxh = max(maxh, h);
        dfs(root->left, h+1);
        dfs(root->right, h+1);
        swap(root->right, root->left);
    }

    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        maxh = 0; dfs(root, 0);
        maxh = 0; dfs(root, 0);
        vector<int> ans;
        for(int q:queries)
            ans.push_back(seen[q]);
        return ans;
    }
};
```
