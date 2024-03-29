
# 24 May 2023

# Questions

---
## [1. Delete Node From Linked List](https://workat.tech/problem-solving/practice/delete-node-linked-list) [(LeetCode)](https://leetcode.com/problems/delete-node-in-a-linked-list/) 

<p>Delete a given node from a singly-linked list. You do not have access to the head of the list. Also, the node to be deleted is not the tail of the linked list.</p>
<h5>Example 1:</h5>
<p><code>1&rarr;2&rarr;3&rarr;4</code></p>
<p>Deleting 2nd node, we get</p>
<p><code>1&rarr;3&rarr;4</code></p>
<h5>Example 2:</h5>
<p><code>1&rarr;3&rarr;4&rarr;1</code></p>
<p>Deleting 3rd node, we get</p>
<p><code>1&rarr;3&rarr;1</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>A number &lsquo;n&rsquo;, denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting elements of the linked list.</li>
<li>A number &lsquo;c&rsquo; denoting the position of the linked list node which is to be deleted.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with <code>n-1</code> space-separated integers denoting the elements of the resultant linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
1 2 3 4
3
3
4 5 6
2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 4
4 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 1000</code><br/>
<code>1 &lt;= element &lt;= 10<sup>5</sup></code></p>

---
## [2. Linked List Palindrome](https://workat.tech/problem-solving/practice/linked-list-palindrome) [(LeetCode)](https://leetcode.com/problems/palindrome-linked-list/) 

<p>Given a non-negative number represented as a linked list, determine whether it is a palindrome or not.</p>
<h4>Example 1:</h4>
<p><i>Number</i> : 1234<br />
<i>Linked list</i> : 1&rarr;2&rarr;3&rarr;4<br />
<i>Result</i> : Not a palindrome</p>
<h4>Example 2:</h4>
<p><i>Number</i> : 1221<br />
<i>Linked list</i> : 1&rarr;2&rarr;2&rarr;1<br />
<i>Result</i> : A palindrome</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>A number &lsquo;n&rsquo;, denoting the length of the number.</li>
<li><em>n</em> space-separated integers, denoting digits of the number.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with <code>1</code> if the number is a palindrome, <code>0</code> otherwise.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
4
3 4 5 3
5
1 2 3 2 1
3
3 1 3
4
1 4 4 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0
1
1
1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>0 &lt;= nodeValue &lt;= 9</code><br/>

---
# [Solution](solution.md)
