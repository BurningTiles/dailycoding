
# 31 Aug 2023

# Questions

---
## [1. Kth Smallest in BST](https://workat.tech/problem-solving/practice/kth-smallest-element-bst) [(LeetCode)](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) 

<p>Given the root node of a binary search tree and a number <code>k</code>, find out the k<sup>th</sup> smallest element (1-indexed) in the BST.</p>
<p>Note: You can assume that k &lt;= number of nodes.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains an integer <strong><i>k</i></strong>.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains an integer with the value of the k<sup>th</sup> smallest element in BST.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
4
7
6 3 21 -1 -1 -1 89
1
12
8 3 9 -1 4 -1 10 -1 -1 -1 12 11
7
4
28 14 -1 11
2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
3
12
14</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
