import java.util.Arrays;

public class solution {
	public static void main(String args[]) {
		int a[][] = {
			{1, 2}, 
			{3, 4}
		};
		System.out.println(Arrays.deepToString(reshape_matrix(a, 1, 4)));
		System.out.println(Arrays.deepToString(reshape_matrix(a, 2, 3)));
	}

	public static int[][] reshape_matrix(int m[][], int x, int y) {
		if(x*y!=m.length*m[0].length)
			return null;

		int tmp[] = new int[x*y], ptr=0;
		for(int i=0; i<m.length; i++)
			for(int j=0; j<m[i].length; j++)
				tmp[ptr++] = m[i][j];

		ptr=0;
		int a[][] = new int[y][x];
		for(int i=0; i<y; i++)
			for(int j=0; j<x; j++)
				a[i][j] = tmp[ptr++];

		return a;
	}
}