# Solution - 22 Oct 2024

---
## [2583. Kth Largest Sum in a Binary Tree](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree)

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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<long long> sums;
        queue<TreeNode*> q;
        
        q.push(root);
        while(q.size()) {
            long long size = q.size(), sum = 0;
            
            while(size--) {
                TreeNode *n = q.front(); q.pop();
                sum += n->val;

                if(n->left) q.push(n->left);
                if(n->right) q.push(n->right);
            }

            sums.push_back(sum);
        }

        if(k > sums.size())
            return -1;

        sort(sums.begin(), sums.end());
        return sums[sums.size() - k];
    }
};
```
