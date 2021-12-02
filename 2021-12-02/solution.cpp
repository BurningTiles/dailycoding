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