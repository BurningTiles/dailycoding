#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> reshapre_matrix(vector<vector<int>> m, int x, int y) {
	vector<vector<int>> a;
	if(x*y!=m.size()*m[0].size())
		return a;

	vector<int> tmp;
	for(int i=0; i<m.size(); i++)
		for(int j=0; j<m[i].size(); j++)
			tmp.push_back(m[i][j]);

	int ptr = 0;
	for(int i=0; i<y; i++) { 
		vector<int> row;
		for(int j=0; j<x; j++)
			row.push_back(tmp[ptr++]);
		a.push_back(row);
	}
	return a;
}

void print(vector<vector<int>> a) {
	if(!a.size()){
		cout << "Null" << endl; return;
	}

	cout << "[";
	for(int i=0; i<a.size(); i++){
		cout << "[";
		for(int j=0; j<a[i].size(); j++)
			cout << a[i][j],
			cout << (j==a[i].size()-1 ? "]" : ", ");
		cout << (i==a.size()-1 ? "]" : ", ");
	}
	cout << endl;
}

signed main() {
	vector<vector<int>> a = {
		{1, 2}, 
		{3, 4}
	};
	print(reshapre_matrix(a, 1, 4));
	print(reshapre_matrix(a, 2, 3));
	return 0;
}