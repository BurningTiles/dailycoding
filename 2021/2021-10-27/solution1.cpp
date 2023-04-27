#include <bits/stdc++.h>
using namespace std;

class Autocomplete{
	struct Node{
		bool isWord = false;
		vector<Node*> child{vector<Node*>(26, NULL)};
	}*Root;
	public:
	Autocomplete(vector<string> words){
		Root = new Node();
		for(auto word:words)
			add(word);
	}

	void add(string word){
		Node *cur = Root;
		int tmp;
		for(auto ch:word){
			if(!cur->child[ch-'a'])
				cur->child[ch-'a'] = new Node();
			cur = cur->child[ch-'a'];
		}
		cur->isWord = true;
	}

	void dfsToList(Node *cur, string word, vector<string> &ans){
		if(cur->isWord)
			ans.push_back(word);
		for(int i=0; i<26; i++)
			if(cur->child[i]){
				word += i+'a';
				dfsToList(cur->child[i], word, ans);
				word.pop_back();
			}
	}

	vector<string> autocomplete(string word){
		Node *cur = Root;
		vector<string> ans;
		for(auto ch:word){
			if(!cur->child[ch-'a'])
				return ans;
			cur = cur->child[ch-'a'];
		}
		dfsToList(cur, word, ans);
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