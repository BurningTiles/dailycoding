# Longest Substring Without Repeating Characters

This problem was recently asked by Apple:

Given a list of words, and an arbitrary alphabetical order, The task is to check whether the given words are sorted lexicographically according to order of alphabets.

Example:
```
Input:
words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

Output: False
```
Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

Example 2:
```
Input:
words = ["zyx", "zyxw", "zyxwy"],
order="zyxwvutsrqponmlkjihgfedcba"

Output: True
```
Explanation: The words are in increasing alphabetical order

Here's a starting point:
```python
def isSorted(words, order):
  # Fill this in.

print isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba")
# False
print isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba")
# True
```

# [Solution](solution.md)