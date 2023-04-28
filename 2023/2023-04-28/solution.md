<!-- # Solution - 27 Apr 2023

### [Cumulative Sum](https://workat.tech/problem-solving/practice/cumulative-sum)
```cpp
vector<int> getCumulativeSum(vector<int> &arr) {
	vector<int> ans(arr.size());
	ans[0] = arr[0];
	for(int i=1; i<arr.size(); i++)
		ans[i] = ans[i-1] + arr[i];
	return ans;
}
```

### [Positive Cumulative Sum](https://workat.tech/problem-solving/practice/positive-cumulative-sum)
```cpp
vector<int> getPositiveCumulativeSum(vector<int> &arr) {
	vector<int> ans;
	int cur = 0;
	for(int i=0; i<arr.size(); i++) {
		cur += arr[i];
		if(cur>0)
			ans.push_back(cur);
	}
	return ans;
}
``` -->