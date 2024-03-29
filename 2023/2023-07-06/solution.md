# Solution - 06 Jul 2023

---
## [1. Find xth Node from End of Linked List](https://workat.tech/problem-solving/practice/find-xth-node-end-linked-list) 

### cpp
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
ListNode* xthNodeFromEnd(ListNode* head, int x) {
	ListNode *tmp = head;
	while(x-- && tmp)
		tmp = tmp->next;
	while(tmp) {
		tmp = tmp->next;
		head = head->next;
	}
	return head;
}
```


---
## [2. Delete Xth Node From End of Linked List](https://workat.tech/problem-solving/practice/delete-xth-node-end-linked-list) [(LeetCode)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) 

### cpp
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

ListNode* removeXthNodeFromEnd(ListNode* head, int x) {
	ListNode *tmp = new ListNode(0), *ptr = head;
	tmp->next = head, head = tmp;
	while(x--) ptr = ptr->next;
	while(ptr) ptr = ptr->next, tmp = tmp->next;
	tmp->next = tmp->next->next;
	return head->next;
}
```
