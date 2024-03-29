# Solution - 19 Jul 2023

---
## [1. Three Sum](https://workat.tech/problem-solving/practice/three-sum) [(LeetCode)](https://leetcode.com/problems/3sum/) 

### cpp
```cpp
vector<vector<int>> threeSum(vector<int> &A) {
	sort(A.begin(), A.end());
	vector<vector<int>> ans;
	int end = A.size()-1;
	
	for(int i=0; i<A.size(); i++) {
		if(A[i]>0) break;
		if(i>0 && A[i]==A[i-1]) continue;
		int j=i+1, k=end;
		while(j<k) {
			if(k<end && A[k]==A[k+1]) {k--; continue;}
			int sum = A[i] + A[j] + A[k];
			if(sum>0) --k;
			else if(sum<0) ++j;
			else ans.push_back({A[i], A[j], A[k]}), ++j, --k;
		}
	}
	
	return ans;
}

/*
// Another Solution
vector<vector<int>> threeSum(vector<int> &A) {
	sort(A.begin(), A.end());
	vector<vector<int>> ans;
	unordered_map<string, bool> mark;
	
	for(int i=1; i<A.size()-1; i++) {
		int l=i-1, r=i+1;
		while(l>=0 && r<A.size()) {
			int sum = A[l] + A[i] + A[r];
			if(sum==0) {
				string s = to_string(A[l]) + "|" + 
					to_string(A[i]) + "|" + to_string(A[r]);
				if(!mark[s]) {
					ans.push_back({A[l], A[i], A[r]});
					mark[s] = true;
				}
				r++, l--;
			} 
			else if(sum<0)
				r++;
			else
				l--;
		}
	}
	
	sort(ans.begin(), ans.end());
	
	return ans;
}
*/
```


---
## [2. Four Sum](https://workat.tech/problem-solving/practice/four-sum) [(LeetCode)](https://leetcode.com/problems/4sum/) 

### cpp
```cpp
vector<vector<int>> fourSum(vector<int> &A, int target) {
	sort(A.begin(), A.end());
	vector<vector<int>> ans;
	int end = A.size()-1;
	
	for(int i=0; i<=end; i++) {
		if(i>0 && A[i]==A[i-1]) continue;
		for(int j=i+1; j<=end; j++) {
			if(j>(i+1) && A[j]==A[j-1]) continue;
			int l=j+1, r=end;
			while(l<r) {
				if(r<end && A[r]==A[r+1]) { --r; continue; }
				long long sum = (long long)A[i]+A[j]+A[l]+A[r];
				if(sum<target) ++l;
				else if(sum>target) --r;
				else ans.push_back({A[i], A[j], A[l], A[r]}), ++l, --r;
			}
		}
	}
	
	return ans;
}
```
