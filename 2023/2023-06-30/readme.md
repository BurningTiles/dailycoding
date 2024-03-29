
# 30 Jun 2023

# Questions

---
## [1. Matrix Search](https://workat.tech/problem-solving/practice/matrix-search) [(LeetCode)](https://leetcode.com/problems/search-a-2d-matrix/) 

<p>Given a matrix, check if the matrix contains a given key.</p>
<p>The matrix has the following properties:</p>
<ul>
<li>Integer in each row is arranged in non-decreasing order from left to right.</li>
<li>The first integer in every row is greater than the last integer of the previous row.</li>
</ul>
<strong>Expected Time Complexity: O(log (n*m))</strong>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>Matrix:
1 2 3
4 5 6
7 8 9
Key: 6
Answer: true</code></pre>

<pre class="plaintext hljs"><code>Matrix:
1 2 3
4 5 6
7 8 9
10 11 12
Key: 15
Answer: false</code></pre>
<h3>Testing</h3>
<h4>Sample Input</h4>
<p>The first line contains 'T' denoting the no. of test cases.</p>
<p>For each test case:</p>
<ul>
<li>The first line contains the numbers 'n' and 'm' denoting the number of rows and columns respectively followed by the key.</li>
<li>The next ‘n’ lines contain ‘m’ space-separated integers denoting elements of a 2-d matrix.</li>
</ul>
<h4>Expected Output</h4>
<p>T lines each contain true/false denoting the answer.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3 3 6
1 2 3
4 5 6
7 8 9
4 3 15
1 2 3
4 5 6
7 8 9
10 11 12</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>true
false</code></pre>

<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= n,m &lt;= 100</code></p>
<p><code>0 &lt;= key &lt;= 10<sup>5</sup></code></p>
<p><code>0 &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code></p>

---
## [2. Median of Row-wise Sorted Matrix](https://workat.tech/problem-solving/practice/median-row-sorted-matrix) [(LeetCode)](https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/) 

<p>Given an <code>n*m</code> matrix which is sorted row-wise, you need to find the median of the matrix.</p>
<p>Median of a group of numbers is the middle element after they are sorted. Both <i>n</i> and <i>m</i> are guaranteed to be odd numbers, therefore there&rsquo;s only one middle number.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>1 2 3
3 3 4
1 1 2
Median: 2</code></pre>
<h3>Testing</h3>
<h4>Input format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has the following lines:</p>
<ul>
<li>The first line contains two space separated integers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the number of rows and columns of the matrix respectively.</li>
<li>The next <i>n</i> lines contain <i>m</i> space-separated integers denoting elements of the matrix.</li>
</ul>
<p><strong>Note:</strong> Each row is sorted.</p>
<h4>Output format</h4>
<p>For each test case, a line containing the the median element.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3 3
1 2 3
3 3 4
1 1 2
3 3
1 2 3
4 5 6
7 8 9
3 5
1 6 7 7 8
2 2 3 3 4
1 2 2 2 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
5
2</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n, m &lt;= 500</code><br/>
<code>1 &lt;= matrix<sub>ij</sub> &lt;= 10<sup>5</sup></code><br/>
<code>n</code> &amp; <code>m</code> are odd numbers.</p>

---
# [Solution](solution.md)
