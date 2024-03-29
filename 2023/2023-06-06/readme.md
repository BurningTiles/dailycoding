
# 06 Jun 2023

# Questions

---
## [1. Identical Binary Trees](https://workat.tech/problem-solving/practice/identical-binary-trees) [(LeetCode)](https://leetcode.com/problems/same-tree/) 

<p>If two binary trees share the exact same structure and have the same node values, they are considered identical.</p>
<p>Given references to the root nodes of two binary trees, find out if the trees are identical or not.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 3 lines:</p>
<ul>
<li>The first line contains two space-separated integers <strong><em>n</em></strong> and <strong><em>m</em></strong> denoting the number of nodes in the trees (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the first binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The second line contains <em>m</em> space-separated integers that will form the first binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with 1 or 0 based on whether the trees are identical or not respectively.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
7 7
1 2 -1 4 -1 5 6
1 2 -1 4 -1 5 6
3 2
6 -1 4
6 1
7 7
8 -1 9 -1 10 11 12
8 -1 9 -1 10 11 12
5 5
28 14 11 -1 48
28 14 10 -1 48
1 1
6
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
1
0
1</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n, m &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>6</sup></code></p>

---
## [2. Symmetric Binary Tree](https://workat.tech/problem-solving/practice/symmetric-binary-tree) [(LeetCode)](https://leetcode.com/problems/symmetric-tree/) 

<p>A binary tree is considered symmetric if it is a mirror image of itself, i.e, it is symmetric around its root node.</p>
<p>Given the root node of a binary tree, determine whether it's symmetric.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/symmetric-binary-tree.svg" alt="symmetric-binary-tree" width="700px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with 1 or 0 based on whether the tree is symmetric or not respectively.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
7
1 2 2 4 -1 -1 4
7
6 4 4 -1 2 -1 2
7
1 2 3 4 -1 -1 4
1
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
0
1</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)
