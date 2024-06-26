# Solution - 03 Apr 2024

---
## [79. Word Search](https://leetcode.com/problems/word-search)

### cpp
```cpp
class Solution {
public:
    bool dfs(vector<vector<char>> &board, string &word, int i=0, int j=0, int k=0) {
        if(k==word.size()) return true;
        if(i<0 || j<0 || i>=board.size() || j>=board[0].size()) return false;
        if(board[i][j]!=word[k]) return false;
        
        board[i][j] = '*';

        bool ans = dfs(board, word, i-1, j, k+1) || 
            dfs(board, word, i+1, j, k+1) ||
            dfs(board, word, i, j-1, k+1) ||
            dfs(board, word, i, j+1, k+1);

        board[i][j] = word[k];
        return ans;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int n=board.size(), m=board[0].size();
        if(word.size() > n*m) return false;

        for(int i=0; i<n; ++i)
            for(int j=0; j<m; ++j)
                if(board[i][j]==word.front() && dfs(board, word, i, j))
                    return true;

        return false;
    }
};
```
