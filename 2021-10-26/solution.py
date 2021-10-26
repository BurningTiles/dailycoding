class Grid:
	def __init__(self, grid):
		self.a = grid

	def area(self, i, j, v):
		if i<0 or i>=len(v) or j<0 or j>=len(v[0]) or v[i][j] or self.a[i][j]==0:
			return 0
		v[i][j] = True
		return self.a[i][j] + self.area(i-1, j, v) + self.area(i+1, j, v) + self.area(i, j+1, v) + self.area(i, j-1, v)

	def max_connected_colors(self):
		visited = [[False for j in range(len(self.a[0]))] for i in range(len(self.a))]
		ans = 0
		for i in range(len(self.a)):
			for j in range(len(self.a[0])):
				ans = max([ans, self.area(i, j, visited)])
		return ans

grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())