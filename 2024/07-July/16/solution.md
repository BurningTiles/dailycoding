# Solution - 16 Jul 2024

---
## [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another)

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
    bool findPath(TreeNode *n, int val, string &path) {
        if(n->val == val)
            return true;
        if(n->left && findPath(n->left, val, path))
            path.push_back('L');
        else if(n->right && findPath(n->right, val, path))
            path.push_back('R');
        return path.size();
    }

    string getDirections(TreeNode* root, int startValue, int destValue) {
        string startPath, destPath;
        findPath(root, startValue, startPath);
        findPath(root, destValue, destPath);

        while(startPath.size() && destPath.size() && startPath.back() == destPath.back()) {
            startPath.pop_back();
            destPath.pop_back();
        }

        return string(startPath.size(), 'U') + string(destPath.rbegin(), destPath.rend());
    }
};
```
