# Solution - 10 Jul 2023

---
## [1. Add One to Linked List](https://workat.tech/problem-solving/practice/add-one-linked-list) 

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
int addOneToNode(ListNode *head) {
	if(head) {
		int tmp = head->data + addOneToNode(head->next);
		head->data = tmp%10;
		return tmp >= 10 ? 1 : 0;
	} else return 1;
}

ListNode* addOneToList(ListNode* head) {
	int carry = addOneToNode(head);
	if(carry) {
		ListNode *tmp = new ListNode(carry);;
		tmp->next = head, head = tmp;
	}
	return head;
}
```


---
## [2. Reorder List](https://workat.tech/problem-solving/practice/reorder-linked-list) [(LeetCode)](https://leetcode.com/problems/reorder-list/) 

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

ListNode* reverseList(ListNode* head) {
	ListNode *ans = NULL, *next;
	while(head) {
		next = head->next;
		head->next = ans;
		ans = head;
		head = next;
	}
	return ans;
}

ListNode* reorderList(ListNode* head) {
	if(!head || !head->next) return head;
	ListNode *slow = head, *fast = head;
	while(fast && fast->next) {
		slow = slow->next;
		fast = fast->next->next;
	}
	ListNode *rev = reverseList(slow->next), *ptr = head, *next;
	slow->next = NULL;
	while(rev) {
		next = rev->next;
		rev->next = ptr->next;
		ptr->next = rev;
		ptr = rev->next;
		rev = next;
	}
	return head;
}
```
