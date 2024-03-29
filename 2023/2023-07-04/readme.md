
# 04 Jul 2023

# Questions

---
## [1. Dutch National Flag](https://workat.tech/problem-solving/practice/dutch-national-flag) [(LeetCode)](https://leetcode.com/problems/sort-colors/) 

<p>Sort an array <code>A</code> where each of the elements belong to the set: <code>{0, 1, 2}</code>.</p>
<p><strong>Expected Time Complexity: O(n)</strong></p>
<p>Try to solve it without storing the count of 0s, 1s and 2s.</p>
<h5>Example:</h5>
<pre class="plaintext hljs"><code>A: [2, 2, 0, 1]
Result: [0, 1, 2, 2]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer 'n' denoting the size of the array <code>A</code>.</li>
<li><em>n</em> space separated integers denoting the elements of array <code>A</code>.</li>
</ul>
<h5>Output Format</h5>
<p>For each test case, the output has a line containing <em>n </em>space separated integers denoting the elements of the sorted array <code>A</code>.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
5
1 0 1 2 2
4
1 0 0 0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0 1 1 2 2
0 0 0 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>0 &lt;= A<sub>i</sub> &lt;= 2</code></p>

---
## [2. k-Substring Vowels](https://workat.tech/problem-solving/practice/k-substring-vowels) 

<p>Given a string s and a number k, find the number of vowels in every substring of size k.</p>
<p>Vowels: <code>['a', 'e', 'i', 'o', 'u']</code></p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>String: "workattech"
k: 3
Here, the substrings of size k and their vowel counts are:
wor =&gt; 1
ork =&gt; 1
rka =&gt; 1
kat =&gt; 1
att =&gt; 1
tte =&gt; 1
tec =&gt; 1
ech =&gt; 1
Answer: [1, 1, 1, 1, 1, 1, 1, 1]</code></pre>

<pre class="plaintext hljs"><code>String: "substring"
k: 2
Here, the substrings of size k and their vowel counts are:
su =&gt; 1
ub =&gt; 1
bs =&gt; 0
st =&gt; 0
tr =&gt; 0
ri =&gt; 1
in =&gt; 1
ng =&gt; 0
Answer: [1, 1, 0, 0, 0, 1, 1, 0]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of test cases.</p>
<p>For each test case, the input contains a string 's' and 'k' denoting the size of the substring.</p>
<h4>Output format</h4>
<p>For each test-cases, the output has n - k + 1 number denoting the elements of the resultant array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
workattech 3
substring 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 1 1 1 1 1 1 1
1 1 0 0 0 1 1 0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>s</code> consists of only lowercase English letters</p>
<p><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= k &lt;= s.length</code></p>

---
# [Solution](solution.md)