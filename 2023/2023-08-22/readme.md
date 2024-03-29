
# 22 Aug 2023

# Questions

---
## [1. Populating Next Right Pointers in Each Node](https://workat.tech/problem-solving/practice/populating-next-right-pointers-in-each-node) [(LeetCode)](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) 

<p>A perfect binary tree is a binary tree in which all interior nodes have two children and all leaves have the same depth or same level.</p>
<p>Given a perfect binary tree which contains an extra <code>next</code> pointer in all the node, populate the <code>next</code> pointers of each node to its next right node.</p>
<p>In nodes with no right nodes, set <code>next</code> to null.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/tree-next-pointer.svg" alt="tree-next-pointer" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree.</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has two lines:
<ul>
<li>The first line contains the number of nodes in the tree.</li>
<li>The second line contains space-separated integers denoting the level order traversal of the tree done using the next pointer for each level.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
1
1
3
1 3 2
7
3 5 6 1 2 7 4
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
1
3
1 3 2
7
3 5 6 1 2 7 4
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
