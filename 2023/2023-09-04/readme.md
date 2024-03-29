
# 04 Sep 2023

# Questions

---
## [1. Serialize and Deserialize Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/serialize-and-deserialize-bst) [(LeetCode)](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) 

<p><a target="_blank" rel="noopener noreferrer" href="https://en.wikipedia.org/wiki/Serialization">Serialization</a> is the process of translating a data structure or object state into a format that can be stored (for example, in a file or memory data buffer) or transmitted (for example, over a computer network) and reconstructed later (possibly in a different computer environment).</p>
<p>The opposite operation, extracting a data structure from a series of bytes, is deserialization.</p>
<p>Design an algorithm to serialize and deserialize a BST.</p>
<ul>
<li>The serialize method should return a string. The format of the string does not matter. Try to keep it as compact as possible to avoid getting TLE/MLE.</li>
<li>The deserialize method when provided the serialized string should return the original BST.</li>
</ul>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary search tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has two lines containing the level order traversal of the tree. The traversal will be printed only if both the trees are identical.</p>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
12
6 2 9 1 5 8 -1 -1 -1 4 -1 7
12
7 3 12 1 5 11 -1 -1 -1 4 -1 10
4
28 14 -1 11</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2 1 3 5 4 7
6 2 9 1 5 8 4 7
7 3 12 1 5 11 4 10
28 14 11</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
