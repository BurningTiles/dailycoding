#include <bits/stdc++.h>
using namespace std;

class Autocomplete{
	vector<string> words;
	public:
	Autocomplete(vector<string> w){
		sort(w.begin(), w.end());
		words = w;
	}

	vector<string> autocomplete(string word){
		int i = lower_bound(words.begin(), words.end(), word) - words.begin();
		word.back()++;
		int j = lower_bound(words.begin()+i, words.end(), word) - words.begin();
		vector<string> ans(&words[i], &words[j]);
		return ans;
	}
};

void print(vector<string> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << "\"" << v[i] << "\"" << (i==v.size()-1 ? "" : ", ");
	cout << "]" << endl;
}

signed main() {
	Autocomplete x({"dog", "dark", "cat", "door", "dodge"});
	print(x.autocomplete("do"));
	return 0;
}