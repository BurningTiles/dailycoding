# Solution - 19 Jun 2023

---
## [1. Best Time to Buy and Sell Stocks](https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock) [(LeetCode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) 

```cpp
int maxProfit(vector<int> &prices) {
	int minPrice = prices[0], ans = 0;
	for(auto &x:prices)
		minPrice = min(x, minPrice),
		ans = max(ans, x-minPrice);
	return ans;
}
```

---
## [2. Best Time to Buy and Sell Stocks II](https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock-ii) [(LeetCode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) 

```cpp
int maxProfit(vector<int> &prices) {
	int ans = 0;
	for(int i=1; i<prices.size(); i++)
		if(prices[i] > prices[i-1]) 
			ans += prices[i]  -prices[i-1];
	return ans;
}
```