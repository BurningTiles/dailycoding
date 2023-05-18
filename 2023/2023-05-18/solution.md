# Solution - 18 May 2023

---
## [1. Kth Element in Linked List](https://workat.tech/problem-solving/practice/kth-element-linked-list) 

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

ListNode* kthElement (ListNode* head, int k) {
	while(--k && head)
		head = head->next;
	return head;
}
```

---
## [2. Add Element at Kth Position in Linked List](https://workat.tech/problem-solving/practice/add-kth-element-linked-list) 

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

ListNode* addAtkthElement (ListNode* head, int k, ListNode* newElement) {
	if(k==1) {
		newElement->next = head;
		return newElement;
	}
	ListNode *ptr = head;
	int i = k-1;
	while(--i)
		ptr = ptr->next;
	newElement->next = ptr->next;
	ptr->next = newElement;
	return ptr;
}
```