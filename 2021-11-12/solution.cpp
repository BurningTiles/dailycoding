#include <bits/stdc++.h>
using namespace std;

bool n_queens_helper(int n, int y, int row[], bool col[], bool diag1[], bool diag2[]){
	if(y==n)
		return true;
	for(int x=0; x<n; x++){
		if(col[x] || diag1[x+y] || diag2[x-y+n-1]) continue;
		col[x] = diag1[x+y] = diag2[x-y+n-1] = true;
		if(n_queens_helper(n, y+1, row, col, diag1, diag2)){
			row[y] = x;
			return true;
		}
		col[x] = diag1[x+y] = diag2[x-y+n-1] = false;
	}
	return false;
}

vector<pair<int, int>> n_queens(int n){
	int a[n]={0};
	bool col[n]={false}, diag1[n*2]={false}, diag2[n*2]={false};
	n_queens_helper(n, 0, a, col, diag1, diag2);
	vector<pair<int, int>> ans;
	for(int i=0; i<n; i++)
		ans.push_back({i, a[i]});
	return ans;
}

void print(vector<pair<int, int>> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << "(" << v[i].first << ", " << v[i].second << ")" << (i==v.size()-1 ? "" : ", ");
	cout << "]\n\n";
	for(int i=0; i<v.size(); i++){
		for(int j=0; j<v.size(); j++)
			cout << (v[i].second==j ? "Q " : ". ");
		cout << endl;
	}
}

signed main() {
	print(n_queens(5));
	return 0;
}