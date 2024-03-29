
# 26 Jun 2023

# Questions

---
## [1. Longest Common Prefix](https://workat.tech/problem-solving/practice/longest-common-prefix) [(LeetCode)](https://leetcode.com/problems/longest-common-prefix/) 

<p>Given a list of strings <code>A</code>, find the longest common prefix among all the strings.</p>
<h5>Example</h5>
<p>A: <code>[&ldquo;abc&rdquo;, &ldquo;abef&rdquo;, &ldquo;abccc&rdquo;, &ldquo;abftg&rdquo;]</code></p>
<p>Longest common prefix: <code>&ldquo;ab&rdquo;</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the number of strings in list A.</li>
<li><em>n</em> space separated strings.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with a string denoting the longest common prefix.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
4
apple apply apollo abracadabra
2
qwerty hello
3
helloworld hell hello
1
hello</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>a

hell
hello</code></pre>
<h4>Constraints</h4>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 100</code><br/>
<code>1 &lt;= A<sub>i</sub> size &lt;= 1000</code></p>

---
## [2. Anagrams](https://workat.tech/problem-solving/practice/anagrams) 

<p>Given two strings <code>A</code> and <code>B</code>, find whether A and B are anagrams of each other or not.</p>
<h5>Example 1</h5>
<p>A: <code>&rdquo;abcd&rdquo;</code></p>
<p>B: <code>&ldquo;dabc&rdquo;</code></p>
<p>A &amp; B are anagrams.</p>
<h5>Example 2</h5>
<p>A: <code>&ldquo;workattech&rdquo;</code></p>
<p>B: <code>&ldquo;worktattch&rdquo;</code></p>
<p>A &amp; B are not anagrams.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input contains three lines</p>
<ul>
<li>two integers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the size of A and B.</li>
<li>string A.</li>
<li>string B.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with 1 if strings are anagrams and 0 otherwise.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
5 5
apple
pplae
5 4
learn
nerd
4 4
abcd
dabc
10 10
workattech
worktattch</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
1
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n, m &lt;= 10<sup>4</sup></code><br/>
Strings should be composed of lowercase English characters.</p>

---
# [Solution](solution.md)
