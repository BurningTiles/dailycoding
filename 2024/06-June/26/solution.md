# Solution - 26 Jun 2024

---
## [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree)

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
    TreeNode* balanceBST(TreeNode* root) {
        // v: where we want to store the TreeNodes in their order
        // construct list using inorder dfs
        vector<TreeNode*> v;
        dfs(root,v);

        // use vector to contruct a balanced tree
        auto ans = build_tree(v, 0, v.size() - 1);
            
        // return tree root node
        return ans;
    }
    
    void dfs(TreeNode* root, vector<TreeNode*> &v) {
        if (root == nullptr)
            return;
        dfs(root->left, v);
        v.push_back(root);
        dfs(root->right, v);
    }
    
    TreeNode* build_tree(const vector<TreeNode*> & v, int left, int right) {
        if(left > right) {
            return nullptr;
        }
        int mid = left + (right - left) / 2;
        auto root = v[mid];
        root-> left = build_tree(v, left, mid - 1);
        root-> right = build_tree(v, mid + 1, right);
        return root;
    }
};
```
