# Solution - 18 Jul 2024

---
## [1530. Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs)

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
    int countPairs(TreeNode* root, int distance) {
        int ans = 0;
        dfs(root, distance, ans);
        return ans;
    }

    vector<int> dfs(TreeNode *root, int d, int &ans) {
        vector<int> p = {};
        if(root == NULL) return p;

        auto left = dfs(root->left, d, ans);
        auto right = dfs(root->right, d, ans);

        if(!left.size() && !right.size()) {
            p.push_back(1);
            return p;
        }

        for(int i=0; i<left.size(); ++i) {
            for(int j=0; j<right.size(); ++j) {
                if(left[i] + right[j] <= d) {
                    ++ans;
                }
            }
        }

        for(int i=0; i<left.size(); ++i) {
            ++left[i];
            p.push_back(left[i]);
        }

        for(int i=0; i<right.size(); ++i) {
            ++right[i];
            p.push_back(right[i]);
        }

        return p;
    }
};
```
