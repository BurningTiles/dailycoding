# Solution - 09 Jan 2024

---
## [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees)

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
    void inorderLeaf(TreeNode* root, vector<int> &leaf) {
        if(root) {
            if(!root->left && !root->right)
                leaf.push_back(root->val);
            else
                inorderLeaf(root->left, leaf),
                inorderLeaf(root->right, leaf);
        }
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaf1, leaf2;
        inorderLeaf(root1, leaf1);
        inorderLeaf(root2, leaf2);

        if(leaf1.size() != leaf2.size()) return false;

        for(int i=0; i<leaf1.size(); ++i)
            if(leaf1[i] != leaf2[i]) return false;

        return true;
    }
};
```
