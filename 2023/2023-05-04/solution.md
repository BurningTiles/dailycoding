# Solution - 4 May 2023

### [Max Consecutive Ones](https://workat.tech/problem-solving/practice/max-consecutive-ones)

```cpp
int getMaxConsecutiveOnes(vector<int> &A) {
	int ans=0, cur=0, last=0;
	for(int i=0; i<A.size(); i++) {
		if(A[i]==1)
			cur = last==1 ? cur+1 : 1;
		last = A[i];
		ans = max(cur, ans);
	}
	return ans;
}
```

### [Arithmetic Sequence](https://workat.tech/problem-solving/practice/arithmetic-sequence)

```cpp
bool isArithmeticSequence(vector<int> &arr) {
	sort(arr.begin(), arr.end());
	if(arr.size()>1) {
		int diff = arr[1] - arr[0];
		for(int i=2; i<arr.size(); i++)
			if(arr[i]-arr[i-1]!=diff)
				return false;
	}
	return true;
}
```
