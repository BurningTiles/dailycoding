#include <bits/stdc++.h>
#define i2d vector<vector<int>>
using namespace std;

i2d rotate(i2d m){
	int rows=m.size();;
	for(int i=0; i<rows; i++)
		for(int j=0; j<i; j++)
			swap(m[i][j], m[j][i]);
	for(int i=0; i<rows; i++)
		reverse(m[i].begin(), m[i].end());
	return m;
}

void print(i2d m){
	for(auto row:m){
		for(auto x:row)
			cout << x << " ";
		cout << endl;}
}

signed main() {
	i2d m = {
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}
	};
	print(rotate(m));
	return 0;
}