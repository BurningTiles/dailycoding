
# 29 Aug 2023

# Questions

---
## [1. Is Binary Tree BST](https://workat.tech/problem-solving/practice/is-binary-tree-bst) [(LeetCode)](https://leetcode.com/problems/validate-binary-search-tree/) 

<p>Every node in a binary search tree holds the following properties:</p>
<ul>
<li>The left subtree has nodes with values less than its own.</li>
<li>The right subtree has nodes with values greater than its own.</li>
<li>The left and right subtrees must also be Binary Search Trees.</li>
</ul>
<p>Given the root node of a binary tree, determine whether it's a binary search tree.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/is-binary-tree-bst.svg" alt="is-binary-tree-bst" width="700px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with 1 or 0 based on whether the binary tree is a binary search tree or not respectively.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
7
6 4 8 1 5 -1 12
3
6 -1 4
2
6 8
6
17 11 28 -1 -1 18
1
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
0
1
1</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
