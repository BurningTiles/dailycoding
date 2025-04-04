# Solution - 20 Dec 2024

---
## [2415. Reverse Odd Levels of Binary Tree](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree)

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
    TreeNode* reverseOddLevels(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int level=0;

        while(q.size()) {
            vector<TreeNode *> tmp;
            int size = q.size();

            for(int i=0; i<size; ++i) {
                TreeNode *n = q.front(); q.pop();
                if(level&1) 
                    tmp.push_back(n);
                if(n->left && n->right) {
                    q.push(n->left);
                    q.push(n->right);
                }
            }

            if(level&1)
                for(int i=0; i<size/2; ++i)
                    swap(tmp[i]->val, tmp[size-i-1]->val);

            ++level;
        }

        return root;
    }
};
```
