# Solution - 12 May 2023

### [Two Sum Sorted](https://workat.tech/problem-solving/practice/two-sum-sorted)

```cpp
bool hasTwoSumZero(vector<int> &A) {
	int l=0, r=A.size()-1, sum;
	while(l<r) {
		sum = A[l] + A[r];
		if(sum<0) l++;
		else if(sum>0) r--;
		else return true;
	}
	return false;
}
```

### [K-Subarray Sum](https://workat.tech/problem-solving/practice/k-subarray-sum)

```cpp
vector<int> kSubarraySum(vector<int> &A, int k) {
	vector<int> ans(A.size() - k + 1);
	for(int i=0; i<k; i++) 
		ans[0] += A[i];
	for(int i=k, j=1; i<A.size(); i++, j++)
		ans[j] = ans[j-1] + A[i] - A[j-1];
	return ans;
}
```
