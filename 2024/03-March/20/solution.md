# Solution - 20 Mar 2024

---
## [1669. Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists)

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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *ans = list1, *ptr = list1, *ptr2 = list2;
        int i=a, j=b;
        
        while(--i) 
            ptr = ptr->next;
        
        while(j>=a)
            ptr->next = ptr->next->next, --j;
        
        while(ptr2->next)
            ptr2 = ptr2->next;
        
        ptr2->next = ptr->next;
        ptr->next = list2;

        return ans;
    }
};
```
