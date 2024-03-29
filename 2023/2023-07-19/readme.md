
# 19 Jul 2023

# Questions

---
## [1. Three Sum](https://workat.tech/problem-solving/practice/three-sum) [(LeetCode)](https://leetcode.com/problems/3sum/) 

<p>Given an array <code>A</code>, find all unique triplets in the array whose sum is equal to zero.</p>
<h5>Example:</h5>
<pre class="plaintext hljs"><code>A: [1, 1, 0, -1, -2]
Triplets: [
  [-2, 1, 1],
  [-1, 0, 1]
]</code></pre>
<p><strong>Note: Each triplet should be sorted. The resultant array should be sorted as well.</strong></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input contains two lines:</p>
<ul>
<li>An integer 'n' denoting the size of the array.</li>
<li><em>n</em> space-separated integers denoting the elements of A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains the following lines.</p>
<ul>
<li>A line containing an integer &lsquo;m&rsquo; denoting the number of unique triplets.</li>
<li><em>m</em> lines contain three integers representing each triplet.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
-1 0 1 2
5
1 -1 9 -8 0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
-1 0 1
2
-8 -1 9
-1 0 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>3 &lt;= n &lt;= 3000</code><br/>
<code>-10<sup>5</sup> &lt;= Ai &lt;= 10<sup>5</sup></code></p>

---
## [2. Four Sum](https://workat.tech/problem-solving/practice/four-sum) [(LeetCode)](https://leetcode.com/problems/4sum/) 

<p>Given an array <code>A</code> and a <code>target</code> value, find all unique quadruples such that their sum is equal to the target value.</p>
<p>Note: The resultant set must not contain any duplicate quadruplets.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [-1 , -3 , -2, -2, 5, 1]
Target: 2
Quadruples: [
 [-1, -3, 5, 1],
 [-2, -2, 5, 1]
]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array <code>A</code>.</li>
<li><em>n</em> space-separated integers denoting the elements of the array <code>A</code>.</li>
<li>The <code>target</code> value.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has the following lines</p>
<ul>
<li>An integer &lsquo;m&rsquo; denoting the number of unique quadruples.</li>
<li>Next <em>m</em> lines each contain four space-separated integers denoting elements whose sum is &lsquo;target&rsquo;.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
5
1 2 3 4 5
11
6
1 2 3 4 5 2
10
1
5
10
10
-2 -7 1 -4 4 -5 6 8 -1 -2
-3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
1 2 3 5
2
1 2 2 5
1 2 3 4
0
6
-7 -5 1 8
-7 -2 -2 8
-7 -1 1 4
-5 -4 -2 8
-5 -2 -2 6
-4 -2 -1 4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>0 &lt;= n &lt;= 200</code><br/>
<code>-10<sup>8</sup> &lt;= A<sub>i</sub> &lt;= 10<sup>8</sup></code><br/>
<code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
