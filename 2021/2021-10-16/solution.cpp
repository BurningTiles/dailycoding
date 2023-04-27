#include <bits/stdc++.h>
using namespace std;

int maxNonAdjacentSum(vector<int> a){
	int include=a[0], exclude=0, tmp;
	for(int i=1; i<a.size(); i++){
		tmp = max(include, exclude);
		include = exclude + a[i];
		exclude = tmp;
	}
	return max(include, exclude);
}

signed main() {
	cout << maxNonAdjacentSum({3, 4, 1, 1}) << endl;
	cout << maxNonAdjacentSum({2, 1, 2, 7, 3}) << endl;
	cout << maxNonAdjacentSum({5, 5, 10, 100, 10, 5}) << endl;

	return 0;
}