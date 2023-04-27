def backtrack(comb, target, cur, counter, ans):
	if target==0:
		ans.append(list(comb))
	if target<=0:
		return
	for i in range(cur, len(counter)):
		val, n = counter[i]
		if n<=0:
			continue
		comb.append(val)
		counter[i] = (val, n-1)
		backtrack(comb, target-val, i, counter, ans)
		counter[i] = (val, n)
		comb.pop()

def sum_combinations(nums, target):
	ans = []
	tmp = {}
	for n in nums:
		tmp[n] = 0
	for n in nums:
		tmp[n] += 1
	counter = [(x, tmp[x]) for x in tmp]
	backtrack([], target, 0, counter, ans)
	return ans

print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
print(sum_combinations([2, 5, 2, 1, 2], 5))