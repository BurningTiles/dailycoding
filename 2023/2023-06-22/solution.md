# Solution - 22 Jun 2023

---
## [1. Flood Fill Image](https://workat.tech/problem-solving/practice/flood-fill-image) [(LeetCode)](https://leetcode.com/problems/flood-fill/) 

### cpp
```cpp
bool valid(vector<vector<int>> &image, int x, int y) {
	return x>=0 && x<image.size() && y>=0 && y<image[0].size();
}

vector<vector<int>> applyFloodFill(vector<vector<int>> &image, int x, int y, int c){
	if(!valid(image, x, y) || image[x][y]==c) return image;
	int initial = image[x][y];
	queue<vector<int>> q;
	q.push({x, y});
	while(q.size()) {
		x = q.front()[0], y = q.front()[1];
		q.pop();
		if(valid(image, x, y) && image[x][y]==initial) {
			image[x][y] = c;
			q.push({x-1, y});
			q.push({x+1, y});
			q.push({x, y-1});
			q.push({x, y+1});
		}
	}
	return image;
}

/*
// DFS way
void dfs(vector<vector<int>> &image, int m, int n, int x, int y, int oldColor, int newColor) {
	if(x<0 || y<0 || x>=m || y>=n || image[x][y]!=oldColor)
		return;
	image[x][y] = newColor;
	dfs(image, m, n, x, y+1, oldColor, newColor);
	dfs(image, m, n, x, y-1, oldColor, newColor);
	dfs(image, m, n, x+1, y, oldColor, newColor);
	dfs(image, m, n, x-1, y, oldColor, newColor);
}

vector<vector<int>> applyFloodFill(vector<vector<int>> &image, int x, int y, int c){
	if(image[x][y]==c) return image;
	dfs(image, image.size(), image[0].size(), x, y, image[x][y], c);
	return image;
}
*/
```


---
## [2. Roman Numeral to Integer](https://workat.tech/problem-solving/practice/roman-to-integer) [(LeetCode)](https://leetcode.com/problems/roman-to-integer/) 

### cpp
```cpp
int romanToInt(string s) {
	unordered_map<char, int> m = { 
		{ 'I' , 1 }, { 'V' , 5 }, { 'X' , 10 },
		{ 'L' , 50 }, { 'C' , 100 }, { 'D' , 500 },
		{ 'M' , 1000 } };
	int ans=m[s.back()];
	for(int i=0; i<s.size()-1; i++)
		ans += (m[s[i]]<m[s[i+1]] ? -m[s[i]] : m[s[i]]);
	return ans;
}
```
### py
```py
class Solution:
	def romanToInt(self, s: str) -> int:
		val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
		ans = val[s[-1]]
		for i in range(0, len(s)-1):
			ans += val[s[i]] if val[s[i]]>=val[s[i+1]] else -val[s[i]]
		return ans
```
