# Maximum Non Adjacent Sum

This problem was recently asked by Google:

Given a list of positive numbers, find the largest possible set such that no elements are adjacent numbers of each other.

Here's some example and some starter code

```python
def maxNonAdjacentSum(nums):
  # Fill this in.
  
print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)

print(maxNonAdjacentSum([5, 5, 10, 100, 10, 5]))
# 110
# Max sum is 5 (index 0) + 100 (index 3) + 5 (index 5)
```

# [Solution](solution.md)