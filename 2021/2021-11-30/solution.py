from functools import lru_cache
def is_knight_on_board(row, col, k):
	@lru_cache(None)
	def rec(x, y, moves):
		if not (0<=x<8 and 0<=y<8): return 0
		if moves==0: return 1
		probability=0
		for r,c in [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]:
			probability += rec(x+r, y+c, moves-1)
		return probability/8
	return rec(row, col, k)

print(is_knight_on_board(0, 0, 1))
print(is_knight_on_board(3, 3, 2))