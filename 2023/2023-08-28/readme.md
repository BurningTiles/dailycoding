
# 28 Aug 2023

# Questions

---
## [1. Delete Node in a Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/delete-node-from-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/delete-node-in-a-bst/) 

<p>Given the root node of a binary search tree and a key, remove the key from the tree and return the root node.</p>
<p>Note: The tree contains only unique values. <strong>Do not assume</strong> that the key is present in the BST.</p>
<p>There can be multiple solutions. You can return the root node containing any of the solutions as long as the tree is a BST.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/delete-bst.svg" alt="delete-bst" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 3 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary search tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains the key value to be removed.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line containing the inorder traversal of the tree.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
7
12
6 2 9 1 5 8 -1 -1 -1 4 -1 7
2
12
7 3 12 1 5 11 -1 -1 -1 4 -1 10
3
4
28 14 -1 11
15</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 3 4 5
1 4 5 6 7 8 9
1 4 5 7 10 11 12
11 14 28</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
