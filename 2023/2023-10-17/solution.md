# Solution - 17 Oct 2023

---
## [1361. Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes)

### cpp
```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        if(n==1) return true;
        vector<int> v(n), valid(n, true);
        for(int i=0; i<n; ++i){
            if(leftChild[i]!=-1) ++v[leftChild[i]];
            if(rightChild[i]!=-1) ++v[rightChild[i]];
        }
        int root = -1;
        for(int i=0; i<n; ++i)
            if(v[i]>1) return false;
            else if(v[i]==0 && root!=-1) return false;
            else if(v[i]==0) root = true;
        if(root==-1) return false;
        
        queue<int> q; q.push(root);
        while(q.size()) {
            int i = q.front(); q.pop();
            if(!valid[i]) return false;
            valid[i] = false;
            if(leftChild[i]!=-1) q.push(leftChild[i]);
            if(rightChild[i]!=-1) q.push(rightChild[i]);
        }
        return true;
    }
};
```
