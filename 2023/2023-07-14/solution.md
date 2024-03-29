# Solution - 14 Jul 2023

---
## [1. Merge Sort Linked List](https://workat.tech/problem-solving/practice/merge-sort-linked-list) [(LeetCode)](https://leetcode.com/problems/sort-list/) 

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
ListNode* getMiddleElementOfLinkedList (ListNode* list) {
	if(!list) return NULL;
	ListNode *fast = list->next, *slow = list;
	while(fast && fast->next)
		fast = fast->next->next,
		slow = slow->next;
	return slow;
}

ListNode* mergeTwoSortedList (ListNode* list1, ListNode* list2) {
	ListNode *head = new ListNode(0), *cur = head;
	while(list1 && list2) {
		if(list1->data <= list2->data)
			cur->next = list1, list1 = list1->next;
		else
			cur->next = list2, list2 = list2->next;
		cur = cur->next;
	}
	if(list1) cur->next = list1;
	if(list2) cur->next = list2;
	return head->next;
}

ListNode* mergeSort(ListNode* head) {
	if(!head || !head->next) return head;
	ListNode *mid = getMiddleElementOfLinkedList(head);
	ListNode *right = mergeSort(mid->next);
	mid->next = NULL;
	ListNode *left = mergeSort(head);
	return mergeTwoSortedList(left, right);
}

/*
// Easy solution with high space complexity.
ListNode* mergeSort(ListNode* head) {
	vector<int> v;
	while(head) v.push_back(head->data), head = head->next;
	sort(v.rbegin(), v.rend());
	for(auto &x:v) {
		ListNode *tmp = new ListNode(x);
		tmp->next = head, head = tmp;
	}
	return head;
}
*/
```


---
## [2. Evaluate Reverse Polish Notation](https://workat.tech/problem-solving/practice/evaluate-reverse-polish-notation) [(LeetCode)](https://leetcode.com/problems/evaluate-reverse-polish-notation/) 

### cpp
```cpp
int evalRPN(vector<string> &tokens) {
	stack<int> stk;
	const string op = "+-*/";
	for(auto &token:tokens) {
		if(op.find(token) != -1) {
			int b = stk.top(); stk.pop();
			int a = stk.top(); stk.pop();
			if(token=="+") stk.push(a+b);
			if(token=="-") stk.push(a-b);
			if(token=="*") stk.push(a*b);
			if(token=="/") stk.push(a/b);
		}
		else
			stk.push(stoi(token));
	}
	return stk.top();
}
```
