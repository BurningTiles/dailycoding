
# 24 Aug 2023

# Questions

---
## [1. Inorder Successor of Node in BST](https://workat.tech/problem-solving/practice/inorder-successor-bst) 

<p>The inorder successor of a node <code>p</code> is the node <code>q</code> that comes just after <code>p</code> in the binary tree's inorder traversal.</p>
<p>Given the root node of a binary search tree and the node <code>p</code>, find the inorder successor of node <code>p</code>. If it does not exist, return <code>null</code>.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/inorder-successor-bst.svg" alt="inorder-successor-bst" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains an integer denoting the 0-based index of p in the above list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains an integer with the value of the inorder successor. In case the successor doesn't exist the value is -1.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
2
7
6 3 21 -1 -1 -1 89
1
12
8 3 9 -1 4 -1 10 -1 -1 -1 12 11
11
4
28 14 -1 11
0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
6
12
-1</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
