#include <bits/stdc++.h>
using namespace std;

int remove_dups(vector<int> &v){
	int j=1;
	for(int i=1; i<v.size(); i++)
		if(v[i]!=v[i-1])
			v[j] = v[i],
			++j;
	v.resize(j);
	return j;
}

signed main() {
	vector<int> v = {1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9};
	cout << remove_dups(v) << endl;
	for(auto &x:v) cout << x << " ";
	cout << endl;

	v = {1, 1, 1, 1, 1, 1};
	cout << remove_dups(v) << endl;
	for(auto &x:v) cout << x << " ";
	cout << endl;
	return 0;
}