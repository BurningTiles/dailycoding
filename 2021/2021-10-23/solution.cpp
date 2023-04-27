#include <bits/stdc++.h>
using namespace std;

bool canBreak(string s, set<string> &wordsSet){
	if(!wordsSet.size() or !s.size()) return false;
	vector<bool> dp(s.size()+1, false);
	dp[0] = true;
	for(int i=0; i<s.size(); i++)
		for(int j=i+1; j<=s.size(); j++)
			if(dp[i] && wordsSet.count(s.substr(i, j-i)))
				dp[j] = true;
	return dp[s.size()];
}

vector<string> findAllConcatenatedWordsInAList(vector<string> words){
	vector<string> ans;
	set<string> wordsSet;
	for(auto word:words)
		wordsSet.insert(word);
	for(auto word:words){
		wordsSet.erase(word);
		if(canBreak(word, wordsSet))
			ans.push_back(word);
		wordsSet.insert(word);
	}
	return ans;
}

void print(vector<string> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << "\"" << v[i] << "\"" << (i==v.size()-1 ? "" : ", ");
	cout << "]" << endl;
}

signed main() {
	print(findAllConcatenatedWordsInAList({"tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"}));
	return 0;
}