#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<string> &ans, string cur, int open, int close, int max) {
	if(cur.size()==max*2){
		ans.push_back(cur);
		return;
	}
	if(open<max)
		cur.push_back('('),
		backtrack(ans, cur, open+1, close, max),
		cur.pop_back();
	if(close<open)
		cur.push_back(')'),
		backtrack(ans, cur, open, close+1, max),
		cur.pop_back();
}

vector<string> generate_brackets(int n){
	vector<string> ans;
	backtrack(ans, "", 0, 0, n);
	return ans;
}

void print(vector<string> a) {
	if(!a.size()){
		cout << "Null" << endl; return;
	}

	cout << "[\'";
	for(int i=0; i<a.size(); i++)
		cout << a[i],
		cout << (i==a.size()-1 ? "\']" : "\', \'");
	cout << endl;
}

signed main() {
	print(generate_brackets(1));
	print(generate_brackets(3));
	return 0;
}