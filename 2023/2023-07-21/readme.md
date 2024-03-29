
# 21 Jul 2023

# Questions

---
## [1. Longest Substring Without Repeat](https://workat.tech/problem-solving/practice/longest-substring-without-repeat) [(LeetCode)](https://leetcode.com/problems/longest-substring-without-repeating-characters/) 

<p>Given a string <code>s</code>, find the length of the longest substring without repeating characters.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code><strong>s:</strong> &ldquo;workattech&rdquo;
<strong>Result:</strong> 6
<strong>Explanation:</strong> Longest vaild substring is &ldquo;workat&rdquo;.</code></pre>
<pre class="plaintext hljs"><code><strong>s:</strong> &ldquo;mississippi&rdquo;
<strong>Result:</strong> 3
<strong>Explanation:</strong> Longest vaild substrings are &ldquo;mis&rdquo; and &ldquo;sip&rdquo;, both of length 3.</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the string.</li>
<li>The string s.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with an integer denoting the length of the longest substring in s having distinct characters.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
10
workattech
11
mississippi</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>6
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>6</sup></code><br/>
<code>The string s consists of lowercase English characters.</code></p>

---
## [2. Distinct Numbers in Window](https://workat.tech/problem-solving/practice/distinct-numbers-window) 

<p>Given an array <code>A</code> and a value <code>k</code>, find the number of distinct elements in each window (subarray) of size <code>k</code>.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [1, 1, 2, 1, 4, 6, 5]
k: 3
Result: [2, 2, 3, 3, 3]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated integers denoting elements of array A.</li>
<li>An integer &lsquo;k&rsquo; denoting the window size.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with (<em>n-k+1)</em> space separated integers denoting the number of different elements in each window of size <em>k</em>.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
7
1 1 2 1 4 6 5
3
4
1 1 1 4
2
5
1 1 2 1 1
2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2 2 3 3 3
1 1 2
1 2 2 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></code><br/>
<code>1 &lt;= k &lt;= n</code></p>

---
# [Solution](solution.md)
