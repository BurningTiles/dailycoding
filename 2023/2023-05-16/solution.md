# Solution - 16 May 2023

---
## [1. Maximum K-Subarray Sum](https://workat.tech/problem-solving/practice/maximum-k-subarray-sum) 

```cpp
int maxKSubarraySum(vector<int> &A, int k) {
	int ans = INT_MIN, cur_sum = 0;
	for(int i=0; i<k; i++) 
		cur_sum += A[i];
	ans = max(ans, cur_sum);
	for(int i=k; i<A.size(); i++) {
		cur_sum = cur_sum + A[i] - A[i-k];
		ans = max(ans, cur_sum);
	}
	return ans;
}
```

---
## [2. Print Linked List](https://workat.tech/problem-solving/practice/print-linked-list) 

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

void printLinkedList (ListNode* head) {
    while(head) {
		cout << head->data << " ";
		head = head->next;
	}
}
```