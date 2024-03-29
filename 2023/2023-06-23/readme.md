
# 23 Jun 2023

# Questions

---
## [1. Integer to Roman Numeral](https://workat.tech/problem-solving/practice/integer-to-roman) [(LeetCode)](https://leetcode.com/problems/integer-to-roman/) 

<p>Given an integer <code>num</code>, convert it to a roman numeral.</p>
<p>Roman numerals are denoted by a combination of some symbols.</p>
<table>
	<thead>
		<tr><th>Value</th><th>Symbol</th></tr>
	</thead>
	<tbody>
		<tr><td>1</td><td>I</td></tr>
		<tr><td>5</td><td>V</td></tr>
		<tr><td>10</td><td>X</td></tr>
		<tr><td>50</td><td>L</td></tr>
		<tr><td>100</td><td>C</td></tr>
		<tr><td>500</td><td>D</td></tr>
		<tr><td>1000</td><td>M</td></tr>
	</tbody>
</table>
<h5>Example 1</h5>
<p>num: <code>10</code></p>
<p>Result: <code>&ldquo;X&rdquo;</code></p>
<h5>Example 2</h5>
<p>s: <code>6</code></p>
<p>Result: <code>&ldquo;VI&rdquo;</code></p>
<h5>Example 3</h5>
<p>s: <code>12</code></p>
<p>Result: <code>&ldquo;XII&rdquo;</code></p>
<p><i>Read about Integer to Roman conversion <a target="_blank" rel="noopener noreferrer" href="https://www.math-only-math.com/roman-numerals.html">here</a></i>.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input contains a line with an integer &lsquo;num&rsquo;.</p>
<h4>Output Format</h4>
<p>For each test case, the output contains one line with a string &lsquo;s&rsquo; denoting the roman denotation of <i>num</i>.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
15
3610
20</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>XV
MMMDCX
XX</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= num &lt;= 4000</code></p>

---
## [2. Substring Search - I](https://workat.tech/problem-solving/practice/substring-search) [(LeetCode)](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) 

<p>Given two strings <code>s1</code> and <code>s2</code>, find the index of the first occurrence of <code>s2</code> in <code>s1</code> as a substring.<br/>
If no such occurence exists, return <code>-1</code>.</p>
<p>This problem is also known as finding needle in a haystack.</p>
<h5>Example 1</h5>
<pre class="plaintext hljs"><code><strong>s1:</strong> &ldquo;helloworld&rdquo;
<strong>s2:</strong> &ldquo;low&rdquo;
<strong>Answer:</strong> 3</code></pre>
<h5>Example 2</h5>
<pre class="plaintext hljs"><code><strong>s1:</strong> &ldquo;workattech&rdquo;
<strong>s2:</strong> &ldquo;technology&rdquo;
<strong>Answer:</strong> -1</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has two lines:</p>
<ul>
<li>A string &ldquo;s1&rdquo;.</li>
<li>A string &ldquo;s2&rdquo;.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line with the value &lsquo;index&rsquo;. If <i>s2</i> is present in <i>s1</i>, <i>index</i> is the the index of the first occurence, otherwise <code>-1</code>.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
competitive
pet
roundandround
round
callofduty
fall</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
0
-1</code></pre>
<h4>Constraint</h4>
<p><code>1 &lt;= T &lt;= 50</code><br/>
<code>1 &lt;= s1.size, s2.size &lt;= 1000</code><br/>
All characters in s1 and s2 are lowercase English alphabets.</p>

---
# [Solution](solution.md)
