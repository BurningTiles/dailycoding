
# 10 Jul 2023

# Questions

---
## [1. Add One to Linked List](https://workat.tech/problem-solving/practice/add-one-linked-list) 

<p>Given a natural number in the form of a linked list, add 1 to it.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>Linked List: 7→8→9
Resultant List: 7→9→0</code></pre>

<pre class="plaintext hljs"><code>Linked List: 9→9→9
Resultant List: 1→0→0→0</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer ‘n’ denoting the length of the linked list.</li>
<li>n space-separated integers denoting the digits of the number.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing integers denoting the digits of the result.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3
7 8 9
3
9 9 9
1
0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>7 9 0
1 0 0 0
1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>0 &lt;= element &lt;= 9</code></p>

---
## [2. Reorder List](https://workat.tech/problem-solving/practice/reorder-linked-list) [(LeetCode)](https://leetcode.com/problems/reorder-list/) 

<p>Given a linked list of the form:</p>
<code>N<sub>0</sub> → N<sub>1</sub> → N<sub>2</sub> → ....N<sub>n-2</sub> → N<sub>n-1</sub></code>
<p>Reorder the list in the following format:</p>
<code>N<sub>0</sub> → N<sub>n-1</sub> → N<sub>1</sub> → N<sub>n-2</sub> → N<sub>2</sub> → ....</code>

<h5>Example</h5>
<pre class="plaintext hljs"><code>Linked list: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
Result: 1 → <span style="background-color: yellow;">9</span> → 2 → <span style="background-color: yellow;">8</span> → 3 → <span style="background-color: yellow;">7</span> → 4 → <span style="background-color: yellow;">6</span> → 5</code></pre>

<pre class="plaintext hljs"><code>Linked list: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
Result: 1 → <span style="background-color: yellow;">8</span> → 2 → <span style="background-color: yellow;">7</span> → 3 → <span style="background-color: yellow;">6</span> → 4 → <span style="background-color: yellow;">5</span></code></pre>
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
9
1 2 3 4 5 6 7 8 9
8
1 2 3 4 5 6 7 8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 9 2 8 3 7 4 6 5
1 8 2 7 3 6 4 5</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>0 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>


---
# [Solution](solution.md)
