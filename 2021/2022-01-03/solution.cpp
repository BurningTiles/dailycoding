#include <bits/stdc++.h>
using namespace std;

int findJudge(int n, vector<vector<int>> trust){
	vector<int> v(n+1, 0);
	for(auto &t:trust)
		v[t[0]]--, v[t[1]]++;
	for(int i=1; i<=n; i++)
		if(v[i]==n-1) return i;
	return -1;
}

signed main() {
	cout << findJudge(2, { {1, 2}}) << endl;
	cout << findJudge(3, { {1, 3}, {2, 3}}) << endl;
	cout << findJudge(3, { {1, 3}, {2, 3}, {3, 1}}) << endl;
	return 0;
}