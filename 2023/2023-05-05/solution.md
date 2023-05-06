# Solution - 5 May 2023

### [Largest Contiguous Sum](https://workat.tech/problem-solving/practice/largest-contiguous)
```cpp
int largestContiguousSum(vector <int> &arr){
    int ans = INT_MIN, cur = 0;
	for(int i=0; i<arr.size(); i++) {
		cur += arr[i];
		ans = max(cur, ans);
		if(cur<0) cur = 0;
	}
	return ans;
}
```

### [Pascal's Triangle](https://workat.tech/problem-solving/practice/pascals-triangle)
```cpp
vector<int> pascalTriangleRow(int rowNo) {
	vector<int> ans(rowNo);
	--rowNo;
	long long temp = 1;
	ans[0] = ans[rowNo] = 1;
	for(int i=1, j=rowNo; i<rowNo; ++i, --j) {
		temp = temp * j / i;
		ans[i] = temp;
	}
	return ans;
}
```