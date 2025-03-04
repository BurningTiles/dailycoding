# Solution - 21 Feb 2025

---
## [1261. Find Elements in a Contaminated Binary Tree](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree)

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
class FindElements {
    unordered_set<int> uset;
public:
    FindElements(TreeNode* root) {
        root->val = 0;
        traverse(root);
    }

    void traverse(TreeNode *root) {
        uset.insert(root->val);
        if(root->left) {
            root->left->val = root->val * 2 + 1;
            traverse(root->left);
        }
        if(root->right) {
            root->right->val = root->val * 2 + 2;
            traverse(root->right);
        }
    }
    
    bool find(int target) {
        return uset.count(target);
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
```
