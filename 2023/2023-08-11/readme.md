
# 11 Aug 2023

# Questions

---
## [1. Construct Binary Tree from Inorder and Postorder Traversal](https://workat.tech/problem-solving/practice/construct-binary-tree-from-inorder-and-postorder-traversal) [(LeetCode)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) 

<p>Given the postorder and inorder traversals of a binary tree, construct and return the binary tree.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/postorder-inorder.svg" alt="postorder-inorder" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 3 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the length of the arrays.</li>
<li>The second line contains <em>n</em> space-separated integers denoting the postorder traversal of the binary tree.</li>
<li>The third line contains <em>n</em> space-separated integers denoting the inorder traversal of the binary tree.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line containing the level order traversal of the tree.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
8
4 7 5 2 8 6 3 1
4 2 7 5 1 8 6 3
5
5 6 4 2 1
5 4 6 2 1
5
11 12 10 9 8
8 9 11 10 12
4
48 14 11 28
14 48 28 11
1
6
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 3 4 5 6 7 8
1 2 4 5 6
8 9 10 11 12
28 14 11 48
6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
