# Solution - 08 Sep 2024

---
## [725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts)

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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        // Get size
        int size = 0;
        for(ListNode *ptr = head; ptr!=NULL; ptr = ptr->next) ++size;

        int ps = size/k, rem = size%k;
        vector<ListNode*> ans(k);
        ListNode *prev = NULL;
        for(int i=0; i<k; ++i, --rem) {
            ans[i] = head;
            for(int j=0; j<ps + (rem>0); j++)
                prev = head, head = head->next;
            if(prev) prev->next = NULL;
        }
        return ans;
    }
};
```
