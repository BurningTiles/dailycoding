
# 25 Sep 2023

# Questions

---
## [1. Maximum path sum in matrix](https://workat.tech/problem-solving/practice/max-path-sum-matrix) 

<p>Given a matrix <code>M</code> of size n*m, find the <i>maximum path sum</i>.</p>
<p>Here, a valid path starts at any element in the first row and ends at any element on the last row.<br/>
Every step we can move one cell in one of three directions:</p>
<ol>
<li>Down</li>
<li>Diagonally to left</li>
<li>Diagonally to right</li>
</ol>
<h5>Example</h5>
<pre class="plaintext hljs"><code>M[][]: 12 22  5  0 20 18
        0  2  5 25 18 17
       12 10  5  4  2  1
        3  8  2 20 10  8
Result: 70
Explanation: Maximum path: 20 &rarr; 25 &rarr; 5 &rarr; 20</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has the following lines:</p>
<ul>
<li>Two space-separated integers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the size of the matrix M.</li>
<li>Next <i>n</i> lines containing <i>m</i> space-separated integers denoting the matrix.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the maximum path sum.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4 6
12 22 5 0 20 18
0 2 5 25 18 17
12 10 5 4 2 1
3 8 2 20 10 8
2 2
3 8
7 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>70
15</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n, m &lt;= 500</code><br/>
<code>0 &lt;= M<sub>ij</sub> &lt;= 10<sup>3</sup></code></p>

---
# [Solution](solution.md)
