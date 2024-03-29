
# 08 Jun 2023

# Questions

---
## [1. Invert Binary Tree](https://workat.tech/problem-solving/practice/invert-binary-tree) [(LeetCode)](https://leetcode.com/problems/invert-binary-tree/) 

<p>Given a binary tree, invert it.</p>
<p>Tree Inversion means that the left child becomes the right child and vice versa. This happens recursively for the subtrees.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/invert-binary-tree.svg" alt="invert-binary-tree" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line containing the level order traversal of the tree.</p>
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
<pre class="plaintext hljs" id="expected-output"><code>1 3 2 6 5 4 8 7 
1 2 4 6 5 
8 9 10 12 11 
28 11 14 48 
6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
## [2. Balanced Binary Tree](https://workat.tech/problem-solving/practice/balanced-binary-tree) [(LeetCode)](https://leetcode.com/problems/balanced-binary-tree/) 

<p>A binary tree is considered balanced if the difference between the heights of the left and the right subtree is not more than 1 for any given node.</p>
<p>Given the root node of a binary tree, determine whether it's height balanced.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/balanced-binary-tree.svg" alt="balanced-binary-tree" width="700px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with 1 or 0 based on whether the tree is balanced or not respectively.</p>
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
<pre class="plaintext hljs" id="expected-output"><code>0
1
0
1
1</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)
