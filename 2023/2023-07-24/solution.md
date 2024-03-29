# Solution - 24 Jul 2023

---
## [1. Longest Substring with K Unique Characters](https://workat.tech/problem-solving/practice/longest-substring-with-k-unique-characters) 

### cpp
```cpp
int longestSubstringWithKUniqueCharacters(string s, int k) {
	unordered_map<char, int> count;
	int j = 0, ans = -1;
	for(int i=0; i<s.size(); i++) {
		count[s[i]]++;
		while(count.size()>k) {
			if(count[s[j]]>1) count[s[j]]--;
			else count.erase(s[j]);
			++j;
		}
		if(count.size() == k)
			ans = max(ans, i-j+1);
	}
	return ans;
}
```


---
## [2. Clone List with Random Pointer](https://workat.tech/problem-solving/practice/clone-list-random-pointer) [(LeetCode)](https://leetcode.com/problems/copy-list-with-random-pointer/) 

### cpp
```cpp
/* This is the ListNode class definition

class ListNode {
	public:
	int data;
	ListNode *next;
	ListNode* random;
	ListNode (int data) {
		this->data = data;
		this->next = NULL;
		this->random = NULL;
	}
};
*/

ListNode* cloneTheLinkedList (ListNode* head) {
	unordered_map<ListNode*, ListNode*> um;
	ListNode *ptr = head;
	while(ptr) {
		um[ptr] = new ListNode(ptr->data);
		ptr = ptr->next;
	}
	ptr = head;
	while(ptr) {
		um[ptr]->next = um[ptr->next];
		um[ptr]->random = um[ptr->random];
		ptr = ptr->next;
	}
	
	return um[head];
}
```
