
# 12 Jun 2023

# Questions

---
## [1. Two Sum in BST](https://workat.tech/problem-solving/practice/two-sum-binary-search-tree) [(LeetCode)](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) 

<p>Given the root node of a binary search tree and a number <code>k</code>, find out if two nodes exist in the tree which add upto k.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/two-sum-binary-search-tree.svg" alt="two-sum-binary-search-tree" width="400px"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
<li>The third line contains an integer <strong><i>k</i></strong>.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains 1 or 0 based on whether the required pair exists or not.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
4
7
6 3 21 -1 -1 -1 89
1
12
8 3 9 -1 4 -1 10 -1 -1 -1 12 11
7
4
28 14 -1 11
2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
1
0</code></pre>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>9</sup></code></p>

---
## [2. Excel Column Number](https://workat.tech/problem-solving/practice/excel-column) [(LeetCode)](https://leetcode.com/problems/excel-sheet-column-number/) 

<p>In excel sheets there are multiple rows and columns. The rows are numbered like 1, 2, 3&hellip;</p>
<p>The columns are numbered like A, B, C,&hellip;X, Y, Z, AA, AB,...AY, AZ, BA,...ZY, ZZ, AAA, AAB,...</p>
<p>Here the column numbers denote the following:</p>
<p>A =&gt; 1</p>
<p>B =&gt; 2</p>
<p>C =&gt; 3</p>
<p>.</p>
<p>.</p>
<p>.</p>
<p>X =&gt; 24</p>
<p>Y =&gt; 25</p>
<p>Z =&gt; 26</p>
<p>.</p>
<p>.</p>
<p>Given an excel column number, find the numerical column number.</p>
<h4>Examples</h4>
<p>Z =&gt; 26</p>
<p>AA =&gt; 27</p>
<p>ABCA =&gt; 19007</p>

<h3>Testing</h3>

<h4>Input Format</h4>
<p>First-line contains ‘T’ denoting the number of test cases.</p>
<p>For each test-case, one line containing a string denoting the column number.</p>

<h4>Output format</h4>
<p>For each test-cases, print a number denoting excel column number.</p>

<h3>Examples</h3>

<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
Z
ABCA</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>26
19007</code></pre>
<h4>Sample Input</h4>
<pre class="plaintext hljs"><code>2
ABC
AAB</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs"><code>731
704</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= t &lt;= 1000</code></p>
<p><code>1 &lt;= Length of column name &lt;= 6</code></p>
<p>Note: Column names will be in uppercase English letters.</p>

---
# [Solution](solution.md)
