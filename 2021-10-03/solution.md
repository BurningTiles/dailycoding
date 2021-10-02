# Reshaping Matrix

### Python
```python
def reshape_matrix(m, x, y):
	if x*y!=len(m)*len(m[0]):
		return None

	tmp, ans, ptr= [x for row in m for x in row], [], 0

	for i in range(y):
		row = []
		for j in range(x):
			row.append(tmp[ptr])
			ptr += 1
		ans.append(row)

	return ans
	
print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
```

### CPP
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> reshapre_matrix(vector<vector<int>> m, int x, int y) {
	vector<vector<int>> a;
	if(x*y!=m.size()*m[0].size())
		return a;

	vector<int> tmp;
	for(int i=0; i<m.size(); i++)
		for(int j=0; j<m[i].size(); j++)
			tmp.push_back(m[i][j]);

	int ptr = 0;
	for(int i=0; i<y; i++) { 
		vector<int> row;
		for(int j=0; j<x; j++)
			row.push_back(tmp[ptr++]);
		a.push_back(row);
	}
	return a;
}

void print(vector<vector<int>> a) {
	if(!a.size()){
		cout << "Null" << endl; return;
	}

	cout << "[";
	for(int i=0; i<a.size(); i++){
		cout << "[";
		for(int j=0; j<a[i].size(); j++)
			cout << a[i][j],
			cout << (j==a[i].size()-1 ? "]" : ", ");
		cout << (i==a.size()-1 ? "]" : ", ");
	}
	cout << endl;
}

signed main() {
	print(reshapre_matrix({{1, 2}, {3, 4}}, 1, 4));
	print(reshapre_matrix({{1, 2}, {3, 4}}, 2, 3));
	return 0;
}
```

### Java
```java
import java.util.Arrays;

public class solution {
	public static void main(String args[]) {
		int a[][] = {{1, 2}, {3, 4}};
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
```