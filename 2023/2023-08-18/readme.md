
# 18 Aug 2023

# Questions

---
## [1. Lowest Common Ancestor in Binary Tree](https://workat.tech/problem-solving/practice/lowest-common-ancestor) [(LeetCode)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) 

<p>The lowest common ancestor of two nodes <code>p</code> and <code>q</code> is the lowest node in the binary tree that has <code>p</code> and <code>q</code> as its descendants.<br/> 
Note: A node is also considered a descendant of itself.</p>
<p>Given the reference to the root node and two nodes p and q in a binary tree, return the reference to the lowest common ancestor of p and q.</p>
<p>Note: You can assume that p and q will be present in the tree.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/lowest-common-ancestor.svg" alt="lowest-common-ancestor" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 3 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains 2 space-separated integers denoting the 0-based index of p and q in the above list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with the value of the lowest common ancestor for p and q.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>6
7
1 2 -1 4 -1 5 6
1 5
3
6 -1 4
0 2
7
8 -1 9 -1 10 11 12
2 5
5
28 14 11 -1 48
4 2
1
6
0 0
7
3 -1 2 1 5 -1 6
3 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
6
9
28
6
1</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)
