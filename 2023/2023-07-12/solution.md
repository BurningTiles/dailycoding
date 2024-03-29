# Solution - 12 Jul 2023

---
## [1. Remove Loop From Linked List](https://workat.tech/problem-solving/practice/remove-loop-linked-list) 

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

void removeLoop(ListNode* list) {
	unordered_map<ListNode *, bool> um;
	ListNode *prev;
	while(list && !um[list]) {
		prev = list;
		um[list] = true;
		list = list->next;
	}
	if(list) prev->next = NULL;
}

/*
// Another approach with less space complexity
void removeLoop(ListNode *list) {
	if(!list || !list->next) return;
	ListNode *slow = list->next, *fast = list->next->next, *prev;
	while(fast && fast->next) {
		if(slow==fast) {
			slow = list;
			break;
		}
		slow = slow->next;
		prev = fast->next;
		fast = fast->next->next;
	}
	if(!fast || !fast->next) return;
	while(slow!=fast)
		prev = fast,
		slow = slow->next,
		fast = fast->next;
	prev->next = NULL;
}
*/
```


---
## [2. Flatten a Multi-Level Linked List](https://workat.tech/problem-solving/practice/flatten-multi-level-linked-list) 

### cpp
```cpp
/* This is the ListNode class definition

class ListNode {
public:
	int data;
	ListNode* next;
	ListNode* down;

	ListNode(int data) {
		this->data = data;
		this->next = NULL;
		this->down = NULL;
	}
};
*/

struct comp {
	bool operator()(ListNode *a, ListNode *b) {
		return a->data > b->data;
	}
};

ListNode* flattenTheLinkedList(ListNode* root) {
	priority_queue<ListNode*, vector<ListNode*>, comp> pq;
	
	while(root)
		pq.push(root), root = root->next;
	
	ListNode *ans = new ListNode(0), *tail = ans;
	while(pq.size()) {
		ListNode *tmp = pq.top();
		pq.pop();
		tail->next = tmp;
		tail = tmp;
		if(tmp->down)
			pq.push(tmp->down),
			tmp->down = NULL;
	}
	return ans->next;
}
```
