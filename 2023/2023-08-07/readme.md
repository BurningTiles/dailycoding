
# 07 Aug 2023

# Questions

---
## [1. Restore IP Addresses](https://workat.tech/problem-solving/practice/restore-ip-addresses) [(LeetCode)](https://leetcode.com/problems/restore-ip-addresses/) 

<p>Given a digit string, return all possible IP Addresses that can be formed from the string.</p>
<p>A valid IP Address contains four integers each in the range of [0, 255]. The four numbers are separated by a '.'. The integers do not have any leading zeros unless the number is itself 0.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>str: "25525511135"
IP: [
    "255.255.11.135",
    "255.255.111.35"
]</code></pre>

<pre class="plaintext hljs"><code>str: "8888"
IP: [
    "8.8.8.8"
]</code></pre>

<pre class="plaintext hljs"><code>str: "0000"
IP: [
    "0.0.0.0"
]</code></pre>

<pre class="plaintext hljs"><code>str: "002500"
IP: [
    "0.0.250.0"
]</code></pre>

<p>The resultant list should be sorted lexicographically. Consider that '<code>.</code>' < '<code>0</code>'.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’, denoting the number of test cases.</p>
<p>For each test case, the input has string str.</p>
<h4>Output Format</h4>
<p>For each test case, the output has the following lines:</p>
<ul>
<li>The first line contains an integer ‘m’ denoting the total no of IP addresses.</li>
<li>The next line contains m space-separated strings denoting the IP addresses.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
25525511135
8888
0000
002500</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
255.255.11.135 255.255.111.35
1
8.8.8.8
1
0.0.0.0
1
0.0.250.0</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 1000</code></p>
<p><code>1 &lt;= n &lt;= 12</code></p>

---
# [Solution](solution.md)
