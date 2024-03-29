
# 14 Jul 2023

# Questions

---
## [1. Merge Sort Linked List](https://workat.tech/problem-solving/practice/merge-sort-linked-list) [(LeetCode)](https://leetcode.com/problems/sort-list/) 

<p>Given a linked list, sort it using merge sort.</p>
<pre class="plaintext hljs"><code>Linked list: 1 → 6 → 2 → 4 → 3 → 5 → 2 → 8 → 4 → 7
Result: 1 → 2 → 2 → 3 → 4 → 4 → 5 → 6 → 7 → 8</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer ‘n’ denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing ‘n’ space-separated integers denoting the resultant linked list elements.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
10
1 6 2 4 3 5 2 8 4 7
10
1 2 2 3 4 4 5 6 7 8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 2 3 4 4 5 6 7 8
1 2 2 3 4 4 5 6 7 8</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>


---
## [2. Evaluate Reverse Polish Notation](https://workat.tech/problem-solving/practice/evaluate-reverse-polish-notation) [(LeetCode)](https://leetcode.com/problems/evaluate-reverse-polish-notation/) 

<p>Given an arithmetic expression in <a href="https://en.wikipedia.org/wiki/Reverse_Polish_notation">Reverse Polish Notation</a> (Postfix Notation), evaluate the value.</p>
<p>Valid operators are <code>+, -, *, /</code>. Each operand may be an integer or another expression.</p>
<p>Note: a/b should return an integer. It is guaranteed that for any division, the divisor won't be 0.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>Expression: ["6", "3", "+", "5", "/"]
Answer: 1
Explanation: ((6 + 3) / 5) =&gt; 9/5 =&gt; 1</code></pre>

<pre class="plaintext hljs"><code>Expression: ["6", "-3", "+", "5", "-"]
Answer: -2
Explanation: ((6 + -3) - 5) =&gt; 3 - 5 =&gt; -2</code></pre>

<pre class="plaintext hljs"><code>Expression: ["6", "3", "2", "+", "*", "5", "/"]
Answer: 6
Explanation: ((6 * (3 + 2)) / 5) =&gt; 6*5/5 =&gt; 6</code></pre>

<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array.</li>
<li>n space-separated strings denoting elements of the expression array.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing an integer representing the answer.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
5
6 3 + 5 /
5
6 -3 + 5 -
7
6 3 2 + * 5 /</code></pre>
Expected Output
<pre class="plaintext hljs" id="expected-output"><code>1
-2
6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>-200 &lt;= tokens<sub>i</sub> &lt;= 200</code></p>


---
# [Solution](solution.md)
