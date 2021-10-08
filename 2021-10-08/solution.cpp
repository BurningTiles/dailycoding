#include <bits/stdc++.h>
using namespace std;

vector<string> generate_brackets(int n){
	vector<string> ans;
	if(n==0)
		return {""};
	for(int i=0; i<n; i++)
		for(string left: generate_brackets(i))
			for(string right: generate_brackets(n-1-i))
				ans.push_back("(" + left + ")" + right);
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