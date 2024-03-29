# Solution - 11 Jul 2023

---
## [1. Rotate a Linked List](https://workat.tech/problem-solving/practice/rotate-linked-list) [(LeetCode)](https://leetcode.com/problems/rotate-list/) 

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

ListNode* rotateListByK(ListNode* head, int k) {
	if(!head || !head->next || !k) return head;
	ListNode *temp = head;
	int len = 1;
	while(temp->next) ++len, temp = temp->next;
	temp->next = head;
	k = len - (k%len);
	for(int i=0; i<k; i++)
		temp = temp->next;
	head = temp->next;
	temp->next = NULL;
	return head;
}

/*
// Another approach
int getLength(ListNode *head) {
	int len = 0;
	while(head) head = head->next, ++len;
	return len;
}

ListNode* rotateListByK(ListNode* head, int k) {
	if(!head || !head->next) return head;
	int len = getLength(head), i=1;
	k = len - (k % len);
	if(k==len) return head;
	ListNode *tmp, *ptr=head;
	while(ptr->next) {
		if(i==k) {
			tmp = ptr->next;
			ptr->next = NULL;
			ptr = tmp;
		}
		else
			ptr = ptr->next;
		++i;
	}
	ptr->next = head;
	head = tmp;
	return head;
}
*/
```


---
## [2. Detect Loop in Linked List](https://workat.tech/problem-solving/practice/detect-loop-linked-list) [(LeetCode)](https://leetcode.com/problems/linked-list-cycle-ii/) 

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

ListNode* getStartingNodeOfLoop(ListNode* list){
	unordered_map<ListNode *, bool> um;
	while(list && !um[list])
		um[list] = true,
		list = list->next;
	return list;
}

/*
// Another approach with O(1) space complexity
ListNode* getStartingNodeOfLoop(ListNode* list){
	if(!list || !list->next) return NULL;
	ListNode *slow = list->next, *fast = list->next->next;
	while(fast && fast->next) {
		if(slow==fast) {
			slow = list;
			break;
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	if(!fast || !fast->next) return NULL;
	while(slow!=fast)
		slow = slow->next,
		fast = fast->next;
	return slow;
}
*/
```
