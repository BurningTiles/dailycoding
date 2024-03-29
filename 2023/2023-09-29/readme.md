
# 29 Sep 2023

# Questions

---
## [1. Unique Paths](https://workat.tech/problem-solving/practice/unique-paths) 

<p>A rat is located at the top-left cell of a m*n matrix. The rat wants to get to the cheese which is at the bottom-right cell of the matrix.</p>
<p>The rat can move only in one of the two directions - down and right. How many unique paths can the rat take to reach the destination?</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/unique-paths.png" width="400px" />
<h5>Examples</h5>
<pre class="plaintext hljs"><code>m:3, n:2
paths: 3

Explanation:
[[Down, Down, Right], [Down, Right, Down], [Right, Down, Down]]</code></pre>
<p>The total number of unique paths can be larger than the largest 32 bit number. Return your answer with module 10<sup>9</sup> + 7.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has two integers m and n.</p>
<h4>Output Format&nbsp;</h4>
<p>For each test case, a line containing an integer denoting the number of unique paths. Return the answer with module 10<sup>9</sup> + 7.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
3 2
2 3
3 3
2 2</code></pre>
<h4>Expected output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
3
6
2</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n, m &lt;= 100</code><br/>

---
# [Solution](solution.md)
