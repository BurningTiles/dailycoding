# Solution - 15 Jul 2024

---
## [2196. Create Binary Tree From Descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions)

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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, pair<TreeNode*, int>> um;

        for(auto &d:descriptions) {
            TreeNode *parent = um[d[0]].first != NULL ? um[d[0]].first : new TreeNode(d[0]);
            TreeNode *child = um[d[1]].first != NULL ? um[d[1]].first : new TreeNode(d[1]);
            
            if(d[2])
                parent->left = child;
            else
                parent->right = child;
            
            um[d[0]].first = parent, um[d[1]].first = child, ++um[d[1]].second;
        }

        for(auto &p:um)
            if(!p.second.second)
                return p.second.first;

        return NULL;
    }
};
```
