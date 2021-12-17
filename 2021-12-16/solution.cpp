#include <bits/stdc++.h>
using namespace std;

vector<int> minHeightTrees(int n, vector<vector<int>> edges){
	if(n==1) return {0};
	if(n==2) return edges[0];
	vector<vector<int>> graph(n);
	vector<int> indegree(n, 0), ans;
	
	for(auto &e:edges){
		graph[e[0]].push_back(e[1]);
		graph[e[1]].push_back(e[0]);
		indegree[e[0]]++;
		indegree[e[1]]++;
	}

	queue<int> q;
	for(int i=0; i<n; i++)
		if(indegree[i]==1) q.push(i), indegree[i]--;
	
	while(!q.empty()){
		int s = q.size();
		ans.clear();
		for(int i=0; i<s; i++){
			int cur = q.front(); q.pop();
			ans.push_back(cur);
			for(auto child:graph[cur]){
				indegree[child]--;
				if(indegree[child]==1) q.push(child);
			}
		}
	}
	return ans;
}

void print(vector<int> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << v[i] << (i==v.size()-1 ? "" : ", ");
	cout << "]\n";
}

signed main() {
	print(minHeightTrees(4, { {1, 0}, {1, 2}, {1, 3}}));
	print(minHeightTrees(6, { {3, 0},{3, 1},{3, 2},{3, 4},{5, 4}}));
	print(minHeightTrees(1, {}));
	print(minHeightTrees(2, { {0, 1}}));
	return 0;
}