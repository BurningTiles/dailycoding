#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool word_search(vector<vector<char>> m, string word){
	int r=m.size(), c=m[0].size(), n=word.size();
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(m[i][j]!=word[0]) continue;
			if(j+n<=c){
				int k=1;
				for(; k<n; k++)
					if(m[i][j+k]!=word[k]) break;
				if(k==n) return true;
			}
			if(i+n<=r){
				int k=1;
				for(; k<n; k++)
					if(m[i+k][j]!=word[k]) break;
				if(k==n) return true;
			}
		}
	}
	return false;
}

signed main() {
	vector<vector<char>> matrix = {
		{'F', 'A', 'C', 'I'},
		{'O', 'B', 'Q', 'P'},
		{'A', 'N', 'O', 'B'},
		{'M', 'A', 'S', 'S'}};

	cout << toBool(word_search(matrix, "FOAM"));

	return 0;
}