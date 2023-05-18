
# 16 May 2023

# Questions

---
## [1. Maximum K-Subarray Sum](https://workat.tech/problem-solving/practice/maximum-k-subarray-sum) 

<p>Given an array and a number k, find the sum of the subarray that has the maximum sum among all the subarrays of size k.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>Array: [3, 5, 6, 2, 4, 7, 8]
k: 3
Here, the subarrays of size k and their sum are:
[3 5 6] =&gt; 14
[5 6 2] =&gt; 13
[6 2 4] =&gt; 12
[2 4 7] =&gt; 13
[4 7 8] =&gt; 19
Answer: 19</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of test cases.</p>
<p>For each test case, the input contains two lines:</p>
<ul>
<li>An integer 'n' denoting the size of the array A and 'k' denoting the size of the subarray.</li>
<li>n space-separated integers denoting elements of the array A.</li>
</ul>
<h4>Output format</h4>
<p>For each test-cases, the output has a single integer denoting the maximum subarray sum.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
7 3
3 5 6 2 4 7 8
6 1
1 3 3 3 4 4</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>19
4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= k &lt;= n</code></p>
<p><code>1 &lt;= A<sub>i</sub> &lt;= 10<sup>4</sup></code></p>

---
## [2. Print Linked List](https://workat.tech/problem-solving/practice/print-linked-list) 

<p>Given a Linked List, print all its nodes.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>List: 1→3→4→7
Print: 1 3 4 7</code></pre>
<p>Note: Each node should be separated by a space. Do not print new line anywhere. The main function will add the new line between tests.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>A number ‘n’, denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
1 3 4 7
3
4 5 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 3 4 7
4 5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 1000</code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>

---
# [Solution](solution.md)
