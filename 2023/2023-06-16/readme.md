
# 16 Jun 2023

# Questions

---
## [1. Find the Missing Number](https://workat.tech/problem-solving/practice/find-the-missing-number) [(LeetCode)](https://leetcode.com/problems/missing-number/) 

<p>You are given a list of integers <code>nums</code> of size <code>n-1</code>. Each number in <code>nums</code> is unique and lies from <code>1</code> to <code>n</code>.</p>
<p>Find the number that is missing from the list.</p>
<h5>Example 1</h5>
<pre class="plaintext hljs"><code><strong>nums:</strong> [3, 1, 4]
<strong>Answer:</strong> 2</code></pre>
<h5>Example 2</h5>
<pre class="plaintext hljs"><code><strong>nums:</strong> [1, 2]
<strong>Answer:</strong> 3</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has two lines:</p>
<ul>
<li>The first line has a positive integer &lsquo;n&rsquo;.</li>
<li>The second line has <i>n-1</i> space-separated integers denoting the list <i>nums</i>.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line containing the missing number.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
3 1 4
3
1 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>2 &lt;= n &lt;= 10000</code></p>

---
## [2. Climbing Stairs](https://workat.tech/problem-solving/practice/climbing-stairs) [(LeetCode)](https://leetcode.com/problems/climbing-stairs/) 

<p>There is a staircase with n steps. You need to reach the top and you can either climb 1 step or 2 steps at a time.</p>
<p>In how many distinct ways can you reach the top of the staircase.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>n: 2
Answer: 2
Explanation: [[1, 1], [2]]</code></pre>
<pre class="plaintext hljs"><code>n: 4
Answer: 5
Explanation: [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>Two space-separated integers &lsquo;n&rsquo; and &lsquo;target&rsquo;.</li>
<li><em>n</em> space-separated integers denoting the available denominations.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the number of possible combinations.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
2
3
4</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
3
5</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 45</code><br/>
<code>1 &lt;= n &lt;= 45</code></p>

---
# [Solution](solution.md)
