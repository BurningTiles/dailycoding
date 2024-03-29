# Solution - 29 Feb 2024

---
## [1609. Even Odd Tree](https://leetcode.com/problems/even-odd-tree)

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
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        bool flag = false;

        while(q.size()) {
            int size = q.size(), last = flag ? INT_MAX : INT_MIN;
            for(int i=0; i<size; ++i) {
                TreeNode *tmp = q.front(); q.pop();
                if(flag) {
                    if(tmp->val < last && !(tmp->val & 1)) last = tmp->val;
                    else return false;
                } else {
                    if(tmp->val > last && tmp->val & 1) last = tmp->val;
                    else return false;
                }
                if(tmp->left) q.push(tmp->left);
                if(tmp->right) q.push(tmp->right);
            }
            flag = !flag;
        }

        return true;
    }
};
```
