# Solution - 25 May 2023

---
## [1. Intersection of Two Linked Lists](https://workat.tech/problem-solving/practice/intersection-two-linked-lists) [(LeetCode)](https://leetcode.com/problems/intersection-of-two-linked-lists/) 

```cpp
/* This is the ListNode class definition

class ListNode {
public:
	int data;
	ListNode* next;

	ListNode(int data) {
		this->data = data;
		this->next = NULL;
	}
};
*/

int length(ListNode *A){
	int size = 0;
	while(A && ++size) A = A->next;
	return size;
}

ListNode* getIntersectionNode(ListNode *A, ListNode *B) {
	int l1 = length(A), l2 = length(B);
	while(l1>l2 && l1--) A=A->next;
	while(l2>l1 && l2--) B=B->next;
	while(l1-- && l2-- && A != B)
		A=A->next, B=B->next;
	return A && B ? A : NULL;
}
```

---
## [2. Remove Duplicates from Sorted Linked List](https://workat.tech/problem-solving/practice/remove-duplicates-sorted-linked-list) [(LeetCode)](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) 

```cpp
/* This is the ListNode class definition

class ListNode {
public:
	int data;
	ListNode* next;

	ListNode(int data) {
		this->data = data;
		this->next = NULL;
	}
};
*/
ListNode* removeDuplicates(ListNode* head) {
	ListNode *tmp = head;
	while(tmp) {
		while(tmp->next && tmp->data==tmp->next->data)
			tmp->next = tmp->next->next;
		tmp = tmp->next;
	}
	return head;
}
```