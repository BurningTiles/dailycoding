
# 27 Jun 2023

# Questions

---
## [1. Row Column Zero](https://workat.tech/problem-solving/practice/row-column-zero) [(LeetCode)](https://leetcode.com/problems/set-matrix-zeroes/) 

<p>Given a matrix, if any of the cells in the matrix is <strong>0</strong>, set all the elements in its row and column to <strong>0</strong>.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>1 1 1        1 0 1
1 0 1   =&gt;   0 0 0
1 1 1        1 0 1

0 1 2        0 0 0
3 4 5   =&gt;   0 4 5
1 2 3        0 2 3

0 1 0        0 0 0
3 4 5   =&gt;   0 4 0
1 2 3        0 2 0

0 1 0        0 0 0
3 0 5   =&gt;   0 0 0
1 2 3        0 0 0</code></pre>

<h3>Testing</h3>

<h5>Input Format</h5>
<p>The first line contains &lsquo;<strong>T</strong>&rsquo; denoting the number of test cases.<br/>
For each test case, the input consists of the following lines:</p>
<ul>
<li>The first line contains two space-separated integers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the number of rows and columns respectively.</li>
<li>The next &lsquo;n&rsquo; lines contains &lsquo;m&rsquo; space-separated integers denoting elements of a 2-D matrix.</li>
</ul>
<h5>Output Format</h5>
<p>For each test case, the output contains n lines, each containing m space-separated integers denoting the resultant matrix.</p>
<h3>Examples</h3>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
2 2
1 0
0 0
3 3
1 1 0
1 1 1
1 1 1
3 3
1 1 1
1 1 0
1 1 1
4 2
1 0
1 0
1 0
1 0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0 0
0 0
0 0 0
1 1 0
1 1 0
1 1 0
0 0 0
1 1 0
0 0
0 0
0 0
0 0</code></pre>

<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= m,n &lt;= 100</code><br/>
<code>1 &lt;= matrix[i][j] &lt;= 10000</code></p>

---
## [2. Matrix Rotation](https://workat.tech/problem-solving/practice/matrix-rotation) [(LeetCode)](https://leetcode.com/problems/rotate-image/) 

<p>Given a matrix, rotate the matrix 90 degrees clockwise.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>Matrix:
1 2 3
4 5 6
7 8 9
After rotation:
7 4 1
8 5 2
9 6 3
Matrix:
1 2
3 4
5 6
After rotation:
5 3 1
6 4 2</code></pre>
<h3>Testing</h3>
<h5>Sample Input</h5>
<p>The first line contains &lsquo;<strong>T</strong>&rsquo; denoting the independent test cases.</p>
<p>For each test case, The first line contains the numbers '<strong>n</strong>' and &lsquo;<strong>m</strong>&rsquo; denoting the number of rows and columns respectively.</p>
<p>The next &lsquo;n&rsquo; lines contains &lsquo;m&rsquo; space-separated integers denoting elements of a 2-d matrix.</p>
<h5>Expected Output</h5>
<p>For each test case, It contains &lsquo;m&rsquo; lines containing &lsquo;n&rsquo; space-separated integers denoting the resultant matrix.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3 3
1 2 3
4 5 6
7 8 9
3 2
1 2
3 4
5 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>7 4 1
8 5 2
9 6 3
5 3 1
6 4 2</code></pre>
<h4>Sample Input</h4>
<pre class="plaintext hljs"><code>1
3 1
1
2
3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs"><code>3 2 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= n,m &lt;= 100</code></p>
<p><code>0 &lt;= matrix[i][j] &lt;= 100000</code></p>

---
# [Solution](solution.md)
