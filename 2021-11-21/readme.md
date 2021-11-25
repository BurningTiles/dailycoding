# Determine If Singly Linked List is Palindrome

This problem was recently asked by Microsoft:

You are given a singly linked list. Determine if it is a palindrome.

```python
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def is_palindrome(node):
  # Fill this in.

node = Node('a', Node('b', Node('b', Node('a'))))

print is_palindrome(node)
# True
```

# [Solution](solution.md)