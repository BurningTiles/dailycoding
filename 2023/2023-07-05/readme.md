
# 05 Jul 2023

# Questions

---
## [1. Maximum k-Substring Vowels](https://workat.tech/problem-solving/practice/maximum-k-substring-vowels) [(LeetCode)](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) 

<p>Given a string s and a number k, find the maximum number of vowels in any substring of size k.</p>
<p>Vowels: <code>['a', 'e', 'i', 'o', 'u']</code></p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>String: "workaattech"
k: 3
Here, the substrings of size k and their vowel counts are:
wor =&gt; 1
ork =&gt; 1
rka =&gt; 1
kaa =&gt; 2
aat =&gt; 2
att =&gt; 1
tte =&gt; 1
tec =&gt; 1
ech =&gt; 1
Answer: 2</code></pre>

<pre class="plaintext hljs"><code>String: "substring"
k: 2
Here, the substrings of size k and their vowel counts are:
su =&gt; 1
ub =&gt; 1
bs =&gt; 0
st =&gt; 0
tr =&gt; 0
ri =&gt; 1
in =&gt; 1
ng =&gt; 0
Answer: 1</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of test cases.</p>
<p>For each test case, the input contains a string 's' and 'k' denoting the size of the substring.</p>
<h4>Output format</h4>
<p>For each test-cases, the output has n - k + 1 number denoting the elements of the resultant array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
workaattech 3
substring 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>s</code> consists of only lowercase English letters</p>
<p><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= k &lt;= s.length</code></p>

---
## [2. Remove Duplicates from Sorted Linked List - II](https://workat.tech/problem-solving/practice/remove-duplicates-sorted-linked-list-ii) [(LeetCode)](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) 

<p>Given a sorted linked list, remove all elements that have duplicates in the Linked List.</p>
<p>After the operation, only those elements should be there which were unique in the original list. Do not change the order of the linked list.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>Linked List: 1→2→2→2→3→3→4→7
After removing duplicates: 1→4→7</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>A number ‘n’, denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers denoting the elements of the resultant linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
8
1 2 2 2 3 3 4 7
3
4 5 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 4 7
4 5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>0 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= element &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)