# Remove duplicates from Linked List

This problem was recently asked by Twitter:

Given a linked list, remove all duplicate values from the linked list.

For instance, given 1 -> 2 -> 3 -> 3 -> 4, then we wish to return the linked list 1 -> 2 -> 4.

```python
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    if not self.next:
      return str(self.val)
    return str(self.val) + " " + str(self.next)

class Solution(object):
  def deleteDuplicates(self, node):
    # Fill this in.


n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print(n)
# 1 2 3 3 4
Solution().deleteDuplicates(n)
print(n)
# 1 2 4
```

# [Solution](solution.md)