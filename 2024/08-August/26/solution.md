# Solution - 26 Aug 2024

---
## [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal)

### cpp
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void traverse(Node *root, vector<int> &ans) {
        if(root) {
            for(auto &ch:root->children)
                traverse(ch, ans);
            ans.push_back(root->val);
        }
    }

    vector<int> postorder(Node* root) {
        vector<int> ans;
        traverse(root, ans);
        return ans;
    }
};
```
