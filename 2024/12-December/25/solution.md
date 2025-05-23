# Solution - 25 Dec 2024

---
## [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row)

### cpp
```cpp
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
    void traverse(TreeNode* root, vector<int> &ans, int level=0) {
        if(root) {
            if(ans.size()>level){
                if(ans[level]<root->val) ans[level] = root->val;
            } else ans.push_back(root->val);
            traverse(root->left, ans, level+1);
            traverse(root->right, ans, level+1);
        }
    }

    vector<int> largestValues(TreeNode* root) {
        vector<int> ans;
        traverse(root, ans);
        return ans;
    }
};
```
