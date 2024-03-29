
# 07 Jun 2023

# Questions

---
## [1. Maximum Depth of Binary Tree](https://workat.tech/problem-solving/practice/maximum-depth-of-binary-tree) [(LeetCode)](https://leetcode.com/problems/maximum-depth-of-binary-tree/) 

<p>Given a binary tree, return its maximum depth.</p>
<p><strong>The depth of a binary tree is the number of nodes from the root node to any of the leaf nodes. The maximum depth is the maximum of the depths across all the paths.</strong></p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/binary-tree-depth.svg" alt="binary-tree-depth" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has an integer denoting the maximum depth of the tree.</p>
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
<pre class="plaintext hljs" id="expected-output"><code>4
4
4
3
1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
## [2. Diameter of Binary Tree](https://workat.tech/problem-solving/practice/diameter-of-binary-tree) [(LeetCode)](https://leetcode.com/problems/diameter-of-binary-tree/) 

<p>Given a binary tree, return the length of the diameter of the tree.</p>
<p>The diameter of a binary tree is the length of the longest path between any two nodes of the tree. The length is the number of edges in the path. The path may or may not include the root node.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/binary-tree-diameter.svg" alt="binary-tree-depth" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has an integer denoting the diameter of the tree.</p>
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
<pre class="plaintext hljs" id="expected-output"><code>6
3
3
3
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
