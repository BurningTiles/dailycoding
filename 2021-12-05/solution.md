# Construct the Rectangle

### Python
```python
def constructRectangle(area):
	s = int(area**(.5))
	while s>1 and area%s!=0:
		s -= 1
	return [area//s, s]

print(constructRectangle(4))
print(constructRectangle(37))
print(constructRectangle(122122))
```

### C++
```cpp
#include <bits/stdc++.h>
#define print(x) cout << "[" << x[0] << ", " << x[1] << "]\n"
using namespace std;

vector<int> constructRectangle(int area){
	int s = sqrt(area);
	while(s>1 && area%s)
		s--;
	return {area/s, s};
}

signed main() {
	vector<int> ans;

	ans = constructRectangle(4);
	print(ans);

	ans = constructRectangle(37);
	print(ans);

	ans = constructRectangle(122122);
	print(ans);

	return 0;
}
```