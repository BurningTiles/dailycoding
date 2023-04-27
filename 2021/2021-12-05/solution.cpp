#include <bits/stdc++.h>
#define print(x) cout << "[" << x[0] << ", " << x[1] << "]\n"
using namespace std;

vector<int> constructRectangle(int area){
	int s = sqrt(area);
	while(s>1 && area%s)
		s--;
	return {area/s, s};
}

signed main() {
	vector<int> ans;

	ans = constructRectangle(4);
	print(ans);

	ans = constructRectangle(37);
	print(ans);

	ans = constructRectangle(122122);
	print(ans);

	return 0;
}