
# 24 Jul 2023

# Questions

---
## [1. Longest Substring with K Unique Characters](https://workat.tech/problem-solving/practice/longest-substring-with-k-unique-characters) 

<p>Given a string <code>str</code> and a number <code>k</code>, find the length of the longest substring in <code>str</code> with exactly <code>k</code> unique characters.</p>
<p>If there are no possible substrings, return -1.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>str: "aabcdaddaf"
k: 3
<strong>Explanation:</strong>
substrings with k unique characters: ["aabc", "abc", "bcd", "cda", "cdad", "cdadd", "cdadda", "daddaf", "addaf", "ddaf", "daf"]
longest substrings: ["cdadda", "daddaf"]
<strong>Result:</strong> 6</code></pre>

<pre class="plaintext hljs"><code>str: "mississippi"
k: 4
<strong>Explanation:</strong>
substrings with k unique characters: ["mississip", "mississipp", "mississippi"]
longest substrings: ["mississippi"]
<strong>Result:</strong> 11</code></pre>

<pre class="plaintext hljs"><code>str: "abcdef"
k: 3
<strong>Explanation:</strong>
substrings with k unique characters: ["abc", "bcd", "cde", "def"]
longest substrings: ["abc", "bcd", "cde", "def"]
<strong>Result:</strong> 3</code></pre>

<pre class="plaintext hljs"><code>str: "aaa"
k: 2
<strong>Explanation:</strong>
substrings with k unique characters: []
longest substrings: []
<strong>Result:</strong> -1</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of test cases.</p>
<p>For each test case, the input has the string str and integer k (space-separated).</p>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with an integer denoting the length of the longest substring in str with exactly k unique characters.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
aabcdaddaf 3
mississippi 4
abcdef 3
aaa 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>6
11
3
-1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= k &lt;= 26</code></p>
<p><code>1 &lt;= str.length &lt;= 10<sup>4</sup></code></p>
<p>The string s consists of lowercase English characters.</p>

---
## [2. Clone List with Random Pointer](https://workat.tech/problem-solving/practice/clone-list-random-pointer) [(LeetCode)](https://leetcode.com/problems/copy-list-with-random-pointer/) 

<p>You are given a linked list L<sub>1</sub> of length <code>n</code>. Each node contains an additional <code>random</code> pointer which could point to any of the nodes in the list, or <code>null</code>.</p>
<p>You need to create a <strong>deep copy</strong> of this list with <i>n</i> newly created nodes. This will create a new linked list L<sub>2</sub>. All nodes of L<sub>2</sub> will have the same value as the corresponding node in L<sub>1</sub>. The next and random pointers will point to nodes in L<sub>2</sub> rather than L<sub>1</sub>.</p>
<p>Return the head of L<sub>2</sub>.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input consists of three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting the value at each node.</li>
<li><em>n</em> space-separated integers denoting the index (<code>0</code> to <code>n-1</code>) of the node to which the random pointer points. -1 if it points to null.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output will consist of n lines.</p>
<p>i<sup>th</sup> line will consists of two space-separated integers x and y for the node at index i.<br />x = value of the node.<br/>
y = index of the node to which the random pointer points.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3
1 2 3
2 1 -1
2
5 6
1 0</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 3
2 2
3 -1
5 6
6 5</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= nodeValue &lt;= 10<sup>5</sup></code></p>

---
# [Solution](solution.md)
