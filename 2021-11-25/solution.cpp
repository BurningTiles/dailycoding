#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

int compare(string s1, string s2, int ord[]){
	int i=0;
	while(i<s1.size() && i<s2.size()){
		if(ord[s1[i]]<ord[s2[i]]) return -1;
		if(ord[s1[i]]>ord[s2[i]]) return 1;
		i++;
	}
	if(s1.size()==s2.size()) return 0;
	return s1.size()<s2.size() ? -1 : 1;
}

bool isSorted(vector<string> v, string order){
	int ord[128] = {0};
	for(int i=0; i<order.size(); i++)
		ord[order[i]] = i;
	for(int i=1; i<v.size(); i++)
		if(compare(v[i-1], v[i], ord)>0)
			return false;
	return true;
}

signed main() {
	cout << toBool(isSorted({"abcd", "efgh"}, "zyxwvutsrqponmlkjihgfedcba")) << endl;
	cout << toBool(isSorted({"zyx", "zyxw", "zyxwy"}, "zyxwvutsrqponmlkjihgfedcba")) << endl;
	return 0;
}