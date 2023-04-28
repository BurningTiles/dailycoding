# Solution - 27 Apr 2023

### [Identical Twins](https://workat.tech/problem-solving/practice/identical-twins)
```cpp
int getIdenticalTwinsCount(vector<int> &arr) {
    unordered_map<int, int> um;
	int pairs = 0;
	for(auto x:arr)
		um[x]++, pairs += um[x]-1;
	return pairs;
}
```

### [Even Number of Digits](https://workat.tech/problem-solving/practice/even-number-of-digits)
```cpp
vector<int> getEvenDigitNumbers(vector<int> &arr) {
    vector<int> ans;
	for(auto num: arr) {
		int len = 0, n=num;
		do {
			++len;
			n /= 10;
		} while(n);
		if(len%2 == 0)
			ans.push_back(num);
	}
	return ans;
}
```