
# 23 May 2023

# Questions

---
## [1. Middle Element of Linked List](https://workat.tech/problem-solving/practice/middle-element-linked-list) [(LeetCode)](https://leetcode.com/problems/middle-of-the-linked-list/) 

<p>Given a linked list, find the middle element and print its value.</p>
<p>If the list has even number of elements, print the first of the two middle elements.</p>
<h5>Examples:</h5>
<p>List: 1&rarr;8&rarr;3</p>
<p>Middle element: 8</p>
<p>List: 1&rarr;3&rarr;8&rarr;5</p>
<p>Middle element: 3</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing an integer denoting the middle element of the linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
3 4 5 6
1
3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>3</sup></code><br/>
<code>1 &lt;= element &lt;= 10<sup>5</sup></code></p>

---
## [2. Merge Two Sorted Linked List](https://workat.tech/problem-solving/practice/merge-sorted-linked-list) [(LeetCode)](https://leetcode.com/problems/merge-two-sorted-lists/) 

<p>Given two sorted linked lists, merge them inplace to produce a singular sorted linked list.</p>
<p>Example:</p>
<p>A: 2&rarr;3&rarr;7</p>
<p>B: 1&rarr;4&rarr;5</p>
<p>Resultant list, after merging A and B:</p>
<p>C: 1&rarr;2&rarr;3&rarr;4&rarr;5&rarr;7</p>
<h3>Testing</h3>
<h4>Input&nbsp;</h4>
<p>The first line contains &lsquo;T&rsquo; denoting the no of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>Two space-separated intergers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the size of the first list and second list respectively.</li>
<li><em>n</em> space-separated integers denoting the elements of first list.</li>
<li><em>m</em> space-separated integers denoting the elements of second list.</li>
</ul>
<h4>Output</h4>
<p>For each test case, a line containing <code>n+m</code> space-separated integers denoting the elements of merged linked list.</p>
<h4>Sample Input&nbsp;</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3 4
1 2 3
2 2 4 5
3 3
2 3 3
1 4 5</code></pre>
<h4>Expected output&nbsp;</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 2 2 3 4 5
1 2 3 3 4 5</code></pre>
<h4>Constraints</h4>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n, m &lt;= 1000</code><br/>
<code>1 &lt;= elements &lt;= 10<sup>6</sup></code><br/>

---
# [Solution](solution.md)
