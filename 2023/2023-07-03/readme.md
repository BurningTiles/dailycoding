
# 03 Jul 2023

# Questions

---
## [1. k-diff pairs](https://workat.tech/problem-solving/practice/k-diff-pairs) [(LeetCode)](https://leetcode.com/problems/k-diff-pairs-in-an-array/) 

<p>Given a sorted array <code>A</code> of size <code>n</code> and a number <code>k</code>, return the number of unique pairs which have a difference of <code>k</code>.</p>
<p><code>|arr[i] - arr[j]| = k</code> where <code>i &lt; j</code></p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [1, 3, 5, 7, 10]
k: 2
Answer: 3</code></pre>

<pre class="plaintext hljs"><code>A: [1, 3, 5, 7, 10]
k: 3
Answer: 1</code></pre>

<pre class="plaintext hljs"><code>A: [1, 3, 5, 7, 10]
k: 1
Answer: 0</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of test cases.</p>
<p>For each test case, the input contains two lines:</p>
<ul>
<li>Two space-separated integers <strong>n</strong> and <strong>k</strong>.</li>
<li><i>n</i> space-separated integers denoting elements of the array A.</li>
</ul>
<h4>Output format</h4>
<p>For each test-cases, the output is an integer denoting the number of k-diff pairs.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
5 2
1 3 5 7 10
5 3
1 3 5 7 10
5 1
1 3 5 7 10</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
1
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>0 &lt;= k &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 10<sup>5</sup></code></p>

---
## [2. Kth element of two sorted lists](https://workat.tech/problem-solving/practice/kth-two-sorted) 

<p>Given two sorted arrays <code>A</code> and <code>B</code>, and another value <code>k</code>, print the k<sup>th</sup> element of the resultant sorted array.</p>
<h5>Example</h5>
<p>A: <code>[1, 2, 3, 4, 5, 6]</code><br/>
B: <code>[3, 4, 4, 5, 6, 6]</code><br/>
Result: <code>[1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6]</code><br/>
3rd element in the array is 3.<br/>
6th element in the array is 4.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case, the input has four lines:</p>
<ul>
<li>The first line contains two integers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the length of the arrays A and B respectively.</li>
<li>The second line contains <em>n</em> space-separated integers denoting the elements of A.</li>
<li>The third line contains <em>m</em> space-separated integers denoting the elements of B.</li>
<li>The fourth line contains &lsquo;k&rsquo; denoting the k<sup>th</sup> element to print.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, print the k<sup>th</sup> smallest number in the merged array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4 4
1 2 3 4
2 3 4 5
3
4 5
1 1 2 3
3 3 4 5 6
5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n, m &lt;= 10000</code><br/>
<code>1 &lt;= A<sub>i</sub>, B<sub>i</sub> &lt;= 100000</code><br/>
<code>1 &lt;= k &lt;= n+m</code></p>

---
# [Solution](solution.md)