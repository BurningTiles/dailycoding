# Word Search

### Python
```python
def word_search(m, word):
	r, c, n = len(m), len(m[0]), len(word)
	for i in range(r):
		for j in range(c):
			if m[i][j]!=word[0]: continue
			if j+n<=c:
				k=1
				while k<n:
					if m[i][j+k]!=word[k]:
						break
					k += 1
				if k==n:
					return True
			if i+n<=r:
				k=1
				while k<n:
					if m[i+k][j]!=word[k]:
						break
					k += 1
				if k==n:
					return True
	return False

matrix = [
	['F', 'A', 'C', 'I'],
	['O', 'B', 'Q', 'P'],
	['A', 'N', 'O', 'B'],
	['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool word_search(vector<vector<char>> m, string word){
	int r=m.size(), c=m[0].size(), n=word.size();
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(m[i][j]!=word[0]) continue;
			if(j+n<=c){
				int k=1;
				for(; k<n; k++)
					if(m[i][j+k]!=word[k]) break;
				if(k==n) return true;
			}
			if(i+n<=r){
				int k=1;
				for(; k<n; k++)
					if(m[i+k][j]!=word[k]) break;
				if(k==n) return true;
			}
		}
	}
	return false;
}

signed main() {
	vector<vector<char>> matrix = {
		{'F', 'A', 'C', 'I'},
		{'O', 'B', 'Q', 'P'},
		{'A', 'N', 'O', 'B'},
		{'M', 'A', 'S', 'S'}};

	cout << toBool(word_search(matrix, "FOAM"));

	return 0;
}
```