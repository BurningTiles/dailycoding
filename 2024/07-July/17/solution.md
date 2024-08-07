# Solution - 17 Jul 2024

---
## [1110. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest)

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
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* helper(TreeNode* node, vector<TreeNode*>& ans, unordered_set<int>& toDelete, bool isRoot) {
        if (!node) return NULL;

        bool deleted = toDelete.find(node->val) != toDelete.end();
        if (isRoot && !deleted)
            ans.push_back(node);

        node->left = helper(node->left, ans, toDelete, deleted);
        node->right = helper(node->right, ans, toDelete, deleted);

        return deleted ? NULL : node;
    }

    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> toDelete;
        vector<TreeNode *> ans;
        
        for (int i = 0; i < to_delete.size(); ++i)
            toDelete.insert(to_delete[i]);
        helper(root, ans, toDelete, true);

        return ans;
    }
};
```
