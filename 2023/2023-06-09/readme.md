
# 09 Jun 2023

# Questions

---
## [1. Search in a Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/search-in-a-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/search-in-a-binary-search-tree/) 

<p>Given the root node of a binary search tree and a key, return the subtree rooted at the node containing the key. If it does not exist, return null.</p>
<p>Note: The tree contains only unique values.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/search-bst.svg" alt="search-bst" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 3 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary search tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains the key value to be searched.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line containing the level order traversal of the subtree.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
2
12
6 2 9 1 5 8 -1 -1 -1 4 -1 7
2
12
8 3 9 -1 4 -1 10 -1 -1 -1 12 11
11
4
28 14 -1 11
0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2 1 3 5 4 7 
2 1 5 4 
11 

</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
## [2. Lowest Common Ancestor in BST](https://workat.tech/problem-solving/practice/lowest-common-ancestor-bst) [(LeetCode)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) 

<p>The lowest common ancestor of two nodes <code>p</code> and <code>q</code> is the lowest node in the binary search tree that has both <code>p</code> and <code>q</code> as its descendants. A node is also considered a descendant of itself.</p>
<p>Given the root node and two nodes p and q in a binary search tree, return their lowest common ancestor.</p>
<p>Note: You can assume that p and q will be present in the tree.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/lowest-common-ancestor-bst.svg" alt="lowest-common-ancestor-bst" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 3 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains 2 space-separated integers denoting the 0-based index of p and q in the above list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with the value of the lowest common ancestor for p and q.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
6 7
7
6 3 21 -1 -1 -1 89
0 6
12
8 3 9 -1 4 -1 10 -1 -1 -1 12 11
1 6
4
28 14 -1 11
0 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>5
6
8
28</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>9</sup></code><br/>
All nodes have unique values.</p>

---
# [Solution](solution.md)
