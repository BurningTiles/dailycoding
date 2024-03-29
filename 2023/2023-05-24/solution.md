# Solution - 24 May 2023

---
## [1. Delete Node From Linked List](https://workat.tech/problem-solving/practice/delete-node-linked-list) [(LeetCode)](https://leetcode.com/problems/delete-node-in-a-linked-list/) 

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

void deleteNode(ListNode* node) {
	node->data = node->next->data;
	node->next = node->next->next;
}
```

---
## [2. Linked List Palindrome](https://workat.tech/problem-solving/practice/linked-list-palindrome) [(LeetCode)](https://leetcode.com/problems/palindrome-linked-list/) 

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

ListNode* reverse(ListNode *list) {
	ListNode *prev=NULL, *next=NULL, *cur=list;
	while(cur) {
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	return prev;
}

ListNode* getMiddle(ListNode *list) {
	if(!list) return NULL;
	ListNode *slow=list, *fast=list->next;
	while(fast && fast->next) {
		fast = fast->next->next;
		slow = slow->next;
	}
	return slow;
}

bool isPalindrome(ListNode *list) {
	if(!list || !list->next) return true;
	ListNode *mid = getMiddle(list), 
		*half2 = reverse(mid->next), 
		*tmp = half2;
	while(half2) {
		if(list->data != half2->data) break;
		list = list->next;
		half2 = half2->next;
	}
	reverse(tmp);
	return !(half2);
}
```