
# 15 Aug 2023

# Questions

---
## [1. Right View of Binary Tree](https://workat.tech/problem-solving/practice/right-view-binary-tree) [(LeetCode)](https://leetcode.com/problems/binary-tree-right-side-view/) 

<p>There are different ways to look at a binary tree. The right view of a binary tree contains the set of nodes that will be visible if you look at the binary tree from the right side.</p>
<p>Given the root node of a binary tree, return an array containing the node elements in the right view, from top to bottom.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/right-view-binary-tree.svg" alt="right-view-binary-tree" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with space-separated integers representing the right view of the  binary tree.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>6
7
1 2 -1 4 -1 5 6
3
6 -1 4
7
8 -1 9 -1 10 11 12
5
28 14 11 -1 48
1
6
7
3 -1 2 1 5 -1 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 4 6
6 4
8 9 10 12
28 11 48
6
3 2 5 6</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)
