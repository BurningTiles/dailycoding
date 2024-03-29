
# 21 Aug 2023

# Questions

---
## [1. Flatten Binary Tree to Linked List](https://workat.tech/problem-solving/practice/flatten-binary-tree-to-linked-list) [(LeetCode)](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) 

<p>Given a binary tree, flatten it to a linked list.</p>
<p>Flattening a binary tree means that:</p>
<ul>
<li>All the right pointers should point to the next node.</li>
<li>All the left pointers should point to null.</li>
<li>The linked list should be in the same order as the preorder traversal of the tree.</li>
</ul>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/flatten-tree.svg" alt="flatten-tree" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has space-separated integers denoting the traversal of the linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
12
1 2 3 4 5 6 -1 -1 -1 7 -1 8
7
1 2 -1 4 -1 5 6
7
8 -1 9 -1 10 11 12
5
28 14 11 -1 48
1
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 4 5 7 3 6 8
1 2 4 5 6
8 9 10 11 12
28 14 48 11
6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
