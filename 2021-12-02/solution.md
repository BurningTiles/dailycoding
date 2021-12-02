# Circle of Chained Words

### Python
```python
def dfs(start, adj, visited):
	visited[start] = True
	for end in adj[start]:
		if not visited[end]:
			dfs(end, adj, visited)

def isConnected(start, adj, mark):
	visited = [False]*26
	dfs(start, adj, visited)

	for i in range(26):
		if mark[i] and not visited[i]: return False
	return True

def chainedWords(words):
	mark = [False]*26
	adj = [[] for _ in range(26)]
	inBound, outBound = [0]*26, [0]*26
	for word in words:
		x=ord(word[0])-97
		y=ord(word[-1])-97
		mark[x], mark[y] = True, True
		inBound[x] += 1
		outBound[y] += 1
		adj[x].append(y)
	for i in range(26):
		if inBound[i]!=outBound[i]: return False
	return isConnected(ord(words[0][0])-97, adj, mark)
		

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

void dfs(int start, vector<int> adj[], vector<bool> &visited){
	visited[start] = true;
	for(auto end:adj[start])
		if(!visited[end])
			dfs(end, adj, visited);
}

bool isConnected(int start, vector<int> adj[], const vector<bool> &mark){
	vector<bool> visited(26, false);
	dfs(start, adj, visited);
	
	for(int i=0; i<26; i++)
		if(mark[i] && !visited[i]) return false;
	return true;
}

bool chainedWords(vector<string> v){
	vector<bool> mark(26, false);
	vector<int> adj[26];
	vector<int> in(26, 0), out(26, 0);
	for(auto str:v){
		int x=str.front()-'a', y=str.back()-'a';
		mark[x] = mark[y] = true;
		in[x]++, out[y]++;
		adj[x].push_back(y);
	}
	for(int i=0; i<26; i++) 
		if(in[i]!=out[i]) return false;
	return isConnected(v.front().front()-'a', adj, mark);
}

signed main() {
	cout << toBool(chainedWords({"apple", "eggs", "snack", "karat", "tuna"})) << endl;
	return 0;
}
```