# Solution - 21 Sep 2023

---
## [1. Collect Jewels](https://workat.tech/problem-solving/practice/collect-jewels) 

### cpp
```cpp
/* This is the JewelStone class definition
class JewelStone {
public:
	int weight, value;
	JewelStone(int weight, int value) {
		this->weight = weight;
		this->value = value;
	}
};
*/
int getMaxValue(vector<JewelStone*> &stones, int capacity) {
	int n = stones.size(), ans[n+1][capacity+1];
	for(int i=0; i<=n; i++) ans[i][0] = 0;
	for(int i=0; i<=capacity; i++) ans[0][i] = 0;
	for(int i=1; i<=n; i++) {
		int w = stones[i-1]->weight, v = stones[i-1]->value;
		for(int j=1; j<=capacity; j++) {
			if(j-w>=0)
				ans[i][j] = max(ans[i-1][j], ans[i-1][j-w] + v);
			else
				ans[i][j] = ans[i-1][j];
		}
	}
	return ans[n][capacity];
}
```
