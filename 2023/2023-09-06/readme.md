
# 06 Sep 2023

# Questions

---
## [1. Matrix Paths](https://workat.tech/problem-solving/practice/matrix-paths) [(LeetCode)](https://leetcode.com/problems/unique-paths/) 

<p>You are given a 2D matrix, and you have to go from top-left to bottom-right. You can only move a cell right or a cell down in each step.<br />Find out how many paths are there to go from the starting cell to the ending cell.</p>
<h5>Example</h5>
<p>Matrix Size: 2 rows, 3 columns</p>
<p>M<sub>00</sub> M<sub>01</sub> M<sub>02</sub><br/>
M<sub>10</sub> M<sub>11</sub> M<sub>12</sub></p>
<p>We have to go from M<sub>00</sub> to M<sub>12</sub>.</p>
<p>M<sub>00</sub> &rarr; M<sub>10</sub> &rarr; M<sub>11</sub> &rarr; M<sub>12</sub> (Down, Right, Right)</p>
<p>M<sub>00</sub> &rarr; M<sub>01</sub> &rarr; M<sub>11</sub> &rarr; M<sub>12</sub> (Right, Down, Right)</p>
<p>M<sub>00</sub> &rarr; M<sub>01</sub> &rarr; M<sub>02</sub> &rarr; M<sub>12</sub> (Right, Right, Down)</p>

<h3>Testing</h3>
<h5>Input Format</h5>
<p>The first line contains a number &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, one line containing space separated numbers 'n' and &lsquo;m&rsquo; denoting the number of rows and columns respectively.</p>

<h5>Output Format</h5>
<p>For each test case, print a line with the count of all possible paths from top-left to bottom-right.</p>

<h3>Examples</h3>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
2 3
3 3
5 5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
6
70</code></pre>

<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 1000</code></p>
<p><code>1 &lt;= m,n &lt;= 20</code></p>

---
# [Solution](solution.md)
