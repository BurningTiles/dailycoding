
# 01 Jun 2023

# Questions

---
## [1. Implement Counting Sort](https://workat.tech/problem-solving/practice/implement-counting-sort) 

<p>Given an array, sort it using counting sort.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains 'T' denoting the no. of test cases.</p>
<p>Next T lines each contain a number 'n' denoting the number of elements, followed by n space-separated numbers denoting the array elements.</p>
<h4>Output Format</h4>
<p>T lines contain n numbers denoting the sorted array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
5 4 2 5 3 1
3 11 4 200</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 3 4 5
4 11 200</code></pre>
<h3>Constraints</h3>
<p><code>0 &lt;= T &lt;= 1000</code></p>
<p><code>1 &lt;= N &lt;= 1000</code></p>
<p><code>-1000 &lt;= array element &lt;= 1000</code></p>

---
## [2. Two Sum](https://workat.tech/problem-solving/practice/two-sum) [(LeetCode)](https://leetcode.com/problems/two-sum/) 

<p>Given an array <code>A</code> and an integer <code>target</code>, find the indices of the two numbers in the array whose sum is equal to the given <code>target</code>.</p>
<p><strong>Note:</strong> The problem has exactly one solution. Do not use the same element twice.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [1, 3, 3, 4]
target: 5
Answer: [0, 3]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has three lines:</p>
<ul>
<li>An integer &rsquo;n&rsquo; denoting the length of the array.</li>
<li><em>n</em> space-separated integers denoting the elements of the array.</li>
<li>An integer &lsquo;target&rsquo; denoting the target value.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has two space-separated integers &lsquo;i&rsquo; and &lsquo;j&rsquo; denoting the indices of the array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
6
8 2 10 4 1 3
9
5
2 4 2 3 2
7</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0 4
1 3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>2 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>-10<sup>9</sup> &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></code><br/>
<code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></p>


---
# [Solution](solution.md)
