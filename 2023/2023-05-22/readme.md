
# 22 May 2023

# Questions

---
## [1. Reverse a Linked List](https://workat.tech/problem-solving/practice/reverse-linked-list) [(LeetCode)](https://leetcode.com/problems/reverse-linked-list/) 

<p>Given a linked list, reverse it.</p>
<h5>Example:</h5>
<p>Input:&nbsp; <code>1&rarr;2&rarr;3&rarr;4&rarr;NULL</code></p>
<p>Output:&nbsp; <code>4&rarr;3&rarr;2&rarr;1&rarr;NULL</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the independent number of test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting the elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing &lsquo;n&rsquo; space-separated integers denoting elements of the reversed linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4
1 2 3 4
3
3 4 5
4
1 0 1 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4 3 2 1
5 4 3
2 1 0 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= element &lt;= 10<sup>5</sup></code></p>

---
## [2. Remove occurrences in Linked List](https://workat.tech/problem-solving/practice/remove-occurences-linked-list) [(LeetCode)](https://leetcode.com/problems/remove-linked-list-elements/) 

<p>Given a linked list and a key, remove all occurrences of the key from the Linked List. Return the head of the resultant list.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>Linked List: 1→2→3→2→4→7→2
Key: 2
After removal: 1→3→4→7</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>A number ‘n’, denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
<li>A number ‘key’ denoting the key to be deleted.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers denoting the elements of the resultant linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
7
1 2 3 2 4 7 2
2
3
4 5 6
8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 3 4 7
4 5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>0 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>
<p><code>1 &lt;= key &lt;= 1000</code></p>

---
# [Solution](solution.md)
