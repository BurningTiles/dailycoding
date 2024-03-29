# Solution - 05 Jul 2023

---
## [1. Maximum k-Substring Vowels](https://workat.tech/problem-solving/practice/maximum-k-substring-vowels) [(LeetCode)](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) 

### cpp
```cpp
int maxKSubstringVowels(string s, int k) {
	const string vovels = "aeiou";
	int count = 0, ans = 0;
	
	for(int i=0; i<k; i++)
		count += vovels.find(s[i]) != -1 ? 1 : 0;
	ans = count;
	
	for(int i=k; i<s.size(); i++) {
		if(vovels.find(s[i-k]) != -1) --count;
		if(vovels.find(s[i]) != -1) ++count;
		ans = max(ans, count);
	}
	
	return ans;
}
```


---
## [2. Remove Duplicates from Sorted Linked List - II](https://workat.tech/problem-solving/practice/remove-duplicates-sorted-linked-list-ii) [(LeetCode)](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) 

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

ListNode* removeDuplicates(ListNode* head) {
	ListNode *ans = new ListNode(0), *ptr = ans;
	ans->next = head;
	while(ptr->next && ptr->next->next) {
		if(ptr->next->data == ptr->next->next->data) {
			int data = ptr->next->data;
			while(ptr->next && ptr->next->data==data)
				ptr->next = ptr->next->next;
		} else
			ptr = ptr->next;
	}
	return ans->next;
}
```