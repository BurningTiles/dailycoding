#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool validate_sudoku(vector<vector<int>> board){
	int b[3][3][10]={0}, x, y;
	for(int i=0; i<9; i++){
		int r[10]={0}, c[10]={0};
		x = i/3;
		for(int j=0; j<9; j++){
			y = j/3;
			if(board[i][j]){
				if(r[board[i][j]] || b[x][y][board[i][j]])
					return false;
				r[board[i][j]]++;
				b[x][y][board[i][j]]++;
			}
			if(board[j][i])
				if(c[board[j][i]]) return false;
				else c[board[j][i]]++;
		}
	}
	return true;
}

signed main() {
	vector<vector<int>> board = {
		{5, 0, 4, 6, 7, 8, 9, 1, 2},
		{6, 0, 2, 1, 9, 5, 3, 4, 8},
		{1, 9, 8, 3, 4, 2, 5, 6, 7},
		{8, 5, 9, 7, 6, 1, 4, 2, 3},
		{4, 2, 6, 8, 5, 3, 7, 9, 1},
		{7, 1, 3, 9, 2, 4, 8, 5, 6},
		{9, 6, 1, 5, 3, 7, 2, 8, 4},
		{2, 8, 7, 4, 1, 9, 6, 3, 5},
		{3, 4, 5, 2, 8, 6, 1, 7, 9}
	};
	cout << toBool(validate_sudoku(board)) << endl;
	return 0;
}