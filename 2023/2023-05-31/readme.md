
# 31 May 2023

# Questions

---
## [1. Balanced Parentheses](https://workat.tech/problem-solving/practice/balanced-parentheses) [(LeetCode)](https://leetcode.com/problems/valid-parentheses/) 

<p>Given a string with the just the six characters - &lsquo;<code>(</code>&rsquo;, &lsquo;<code>)</code>&rsquo;, &lsquo;<code>{</code>&rsquo;, &lsquo;<code>}</code>&rsquo;, &lsquo;<code>[</code>&rsquo; and &lsquo;<code>]</code>&rsquo;. Determine if the string is balanced.</p>
<p>A string is balanced if all brackets exist in pairs and are closed in the correct order.</p>
<h5>Example:</h5>
<p>String: <code>({})[]</code></p>
<p>Result: <code>Balanced</code></p>
<p>String: <code>{()})(</code></p>
<p>Result: <code>Not Balanced</code></p>
<p>String: <code>{(})[]</code></p>
<p>Result: <code>Not Balanced</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case, a line containing a parentheses string.</p>
<h4>Output Format</h4>
<p>For each test case, a line containing <code>1</code> or <code>0</code> if the string is valid or not respectively.</p>
<h4>Sample Input&nbsp;</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
({})[]
{()})(
{(})[]</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= String Length &lt;= 10<sup>4</sup></code></p>

---
## [2. Implement Min Stack](https://workat.tech/problem-solving/practice/min-stack) [(LeetCode)](https://leetcode.com/problems/min-stack/) 

<p>Implement a stack that supports the following operations in O(1) time complexity:</p>
<ul>
<li><code>push(x)</code> : Push the element x onto the stack.</li>
<li><code>pop()</code> : Removes the element at the top of the stack.</li>
<li><code>top()</code> : Get the topmost element of the stack.</li>
<li><code>getMin()</code> : Get the minimum element in the stack.</li>
</ul>
<p>Assume that <code>pop</code>, <code>top</code> and <code>getMin</code> will only be called on non-empty stack.</p>
<h3>Example</h3>
<pre class="plaintext hljs"><code>push(1)
push(2)
push(-1)
getMin() &rarr; -1
pop()
top() &rarr; 2
getMin() &rarr; 1</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case, the input consists of the following lines:</p>
<ul>
<li>First line consists of an integer &lsquo;n&rsquo; denoting the number of operations to be performed on the stack.</li>
<li>The next <i>n</i> lines contain one of the following:</li>
<ul>
<li><code>push x</code>, where x is the element to be added to stack.</li>
<li><code>pop</code></li>
<li><code>top</code></li>
<li><code>getMin</code></li>
</ul>
</ul>
<h4>Output Format</h4>
<p>For each test case, one line containing space-separated values containing the results of <code>pop</code>, <code>top</code>, <code>getMin</code> in the order they are called.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>1
7
push 1
push 2
push -1
getMin
pop
top
getMin</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>-1 2 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>-10<sup>5</sup> &lt;= x &lt;= 10<sup>5</sup></code></p>
<p><code>pop</code>, <code>top</code> and <code>getMin</code> will only be called upon non-empty stack.</p>

---
# [Solution](solution.md)
