# Solution - 04 Jul 2023

---
## [1. Dutch National Flag](https://workat.tech/problem-solving/practice/dutch-national-flag) [(LeetCode)](https://leetcode.com/problems/sort-colors/) 

### cpp
```cpp
void sortTheArray (vector<int> &A) {
	int left=0, right=A.size()-1;
	while(left<A.size() && A[left]==0) ++left;
	for(int i=left; i<=right; i++)
		if(A[i]==0) swap(A[i--], A[left++]);
		else if (A[i]==2) swap(A[i--], A[right--]);
}
```


---
## [2. k-Substring Vowels](https://workat.tech/problem-solving/practice/k-substring-vowels) 

### cpp
```cpp
vector<int> kSubstringVowels(string s, int k) {
	const string vovels = "aeiou";
	vector<int> ans;
	int count = 0;
	for(int i=0, j=-k+1; i<s.size(); i++, j++) {
		if(vovels.find(s[i]) != -1) ++count;
		if(j >= 0) {
			ans.push_back(count);
			if(vovels.find(s[j]) != -1) --count;
		}
	}
	return ans;
}
```