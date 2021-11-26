public class solution {
	public static void main(String args[]) {
		int board[][] = {
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
		System.out.println(validate_sudoku(board));
	}

	/* public static boolean validate_sudoku1(int board[][]){
		
		// rows
		for(int i=0; i<9; i++){
			int count[] = new int[10];
			for(int j=0; j<9; j++){
				if(board[i][j]==0) continue;
				if(count[board[i][j]]>0) return false;
				else count[board[i][j]]++;
			}
		}

		// columns
		for(int i=0; i<9; i++){
			int count[] = new int[10];
			for(int j=0; j<9; j++){
				if(board[i][j]==0) continue;
				if(count[board[j][i]]>0) return false;
				else count[board[j][i]]++;
			}
		}

		// compartment
		for(int i=0; i<9; i++){
			int cnt[][][] = new int[3][3][10], x, y;
			x = i/3;
			for(int j=0; j<9; j++){
				y = j/3;
				if(board[i][j]==0) continue;
				if(cnt[x][y][board[i][j]]>0) return false;
				else cnt[x][y][board[i][j]]++;
			}
		}

		return true;
	} */

	public static boolean validate_sudoku(int board[][]){
		int b_count[][][]=new int[3][3][10], x, y;
		for(int i=0; i<9; i++){
			int r_count[]=new int[10], c_count[]=new int[10];
			x = i/3;
			for(int j=0; j<9; j++){
				y = j/3;
				if(board[i][j]>0){
					if(r_count[board[i][j]]>0 || b_count[x][y][board[i][j]]>0) return false;
					r_count[board[i][j]]++;
					b_count[x][y][board[i][j]]++;
				}
				if(board[j][i]>0){
					if(c_count[board[j][i]]>0) return false;
					c_count[board[j][i]]++;
				}
			}
		}
		return true;
	}
}