# Solution - 10 Sep 2024

---
## [2807. Insert Greatest Common Divisors in Linked List](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list)

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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode *ptr = head;
        
        while(ptr && ptr->next) {
            ListNode *tmp = new ListNode(__gcd(ptr->val, ptr->next->val), ptr->next);
            ptr->next = tmp;
            ptr = ptr->next->next;
        }

        return head;
    }
};
```
