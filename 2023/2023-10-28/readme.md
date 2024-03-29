
# 28 Oct 2023

# Questions

---
## [1. Word Break](https://workat.tech/problem-solving/practice/word-break) 

<p>You are given a string <code>s</code> and a word list <code>w</code> which is a list of unique strings. You have to determine if <code>s</code> can be broken down into a sequence of words where each word is an element in <code>w</code>.</p>
<h5>Examples:</h5>
<pre class="plaintext hljs"><code>s: &ldquo;workattech&rdquo;
w: [&ldquo;tech&rdquo;, &ldquo;work&rdquo;, &ldquo;problem&rdquo;, &ldquo;at&rdquo;]
Result: true</code></pre>
<pre class="plaintext hljs"><code>s: &ldquo;roundandround&rdquo;
w: [&ldquo;and&rdquo;, &ldquo;round&rdquo;]
Result: true</code></pre>
<pre class="plaintext hljs"><code>s: &ldquo;helloworld&rdquo;
w: [&ldquo;hi&rdquo;, &ldquo;world&rdquo;]
Result: false</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>The string <code>s</code>.</li>
<li>An integer &lsquo;n&rsquo; denoting the size of the word list <code>w</code>.</li>
<li><em>n</em> space-separated strings denoting the elements of the word list <code>w</code>.</li>
</ul>
<h4>Expected Output</h4>
<p>For each test case, a line containing <code>1</code> or <code>0</code> depending on whether the string <code>s</code> can be partitioned or not respectively..</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
workattech
4
tech work problem at
roundandround
2
and round
helloworld
2
hi world</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
1
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= s length &lt;= 50</code><br/>
<code>1 &lt;= w size &lt;= 10</code><br/>
<code>1 &lt;= w<sub>i</sub> length &lt;= 10</code></p>

---
# [Solution](solution.md)
