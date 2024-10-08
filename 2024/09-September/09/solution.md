# Solution - 09 Sep 2024

---
## [2326. Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv)

### cpp
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> ans(m, vector<int>(n, -1));
        int l=0, r=n-1, t=0, b=m-1;

        while(l<=r && t<=b) {
            for(int i=l; i<=r && head; ++i) {
                ans[t][i] = head->val;
                head = head->next;
            }
            ++t;

            for(int i=t; i<=b && head; ++i) {
                ans[i][r] = head->val;
                head = head->next;
            }
            --r;

            for(int i=r; i>=l && head; --i) {
                ans[b][i] = head->val;
                head = head->next;
            }
            --b;

            for(int i=b; i>=t && head; --i) {
                ans[i][l] = head->val;
                head = head->next;
            }
            ++l;
        }

        return ans;
    }
};
```
