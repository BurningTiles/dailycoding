#include <bits/stdc++.h>
using namespace std;

int findKthLargest(vector<int> n, int k){
	sort(n.begin(), n.end());
	return n[n.size()-k];
}

signed main() {
	cout << findKthLargest({8, 7, 2, 3, 4, 1, 5, 6, 9, 0}, 3) << endl;
	return 0;
}