
# 20 Jul 2023

# Questions

---
## [1. Longest Consecutive Sequence](https://workat.tech/problem-solving/practice/longest-consecutive-sequence) [(LeetCode)](https://leetcode.com/problems/longest-consecutive-sequence/) 

<p>Given an array of integers <code>A</code>, find the length of the longest consecutive elements sequence.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [24, 2, 34, 1, 3, 4]
Result: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].</code></pre>
<pre class="plaintext hljs"><code>A: [24, 2, 34, 1, 3, 4, 3, -1, 28, 0]
Result: 6
Explanation: The longest consecutive sequence is [-1, 0, 1, 2, 3, 4].</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated integers denoting the elements of the array A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains one line with an integer denoting the length of the longest increasing sequence.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
6
24 2 34 1 3 4
10
24 2 34 1 3 4 3 -1 28 0
4
5 7 9 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
6
1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>-10<sup>9</sup> &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></code></p>

---
## [2. Longest Subarray with Zero Sum](https://workat.tech/problem-solving/practice/longest-subarray-zero-sum) 

<p>Given an array <code>A</code>, find the length of the longest subarray which has a sum equal to <code>0</code>.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [3, 0, -1, -2, 3, 0, -2]
Result: 5
Explanation: Longest Subarray with sum 0: [0, -1, -2, 3, 0]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated integers denoting the elements of the array A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the length of the longest subarray with a sum equal to 0.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
7
3 0 -1 -2 3 0 -2
9
1 2 3 4 5 0 0 -1 1
4
1 -4 2 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>5
4
4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>-10<sup>9</sup> &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
