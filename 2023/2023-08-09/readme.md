
# 09 Aug 2023

# Questions

---
## [1. Binary Tree Zigzag Level Order Traversal](https://workat.tech/problem-solving/practice/zigzag-level-order-traversal) [(LeetCode)](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) 

<p>There are different ways to traverse a binary tree. The zigzag level order traversal of a binary tree covers all the nodes of the tree such that each level is traversed <i>left to right</i> or <i>right to left</i> alternatively.</p>
<p>Given the root node of a binary tree, return an array depicting the zigzag level order traversal.</p>
<p>Note: The first level is traversed left to right.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/zigzag-level-order-traversal.svg" alt="zigzag-level-order-traversal" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with space-separated integers representing the zigzag level order traversal of the binary tree.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
7
1 2 -1 4 -1 5 6
3
6 -1 4
7
8 -1 9 -1 10 11 12
5
28 14 11 -1 48
1
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 4 6 5
6 4
8 9 10 12 11
28 11 14 48
6</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)
