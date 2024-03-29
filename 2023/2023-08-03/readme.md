
# 03 Aug 2023

# Questions

---
## [1. Letter Combinations of a Phone Number](https://workat.tech/problem-solving/practice/letter-combinations-of-a-phone-number) [(LeetCode)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 

<p>Given a string containing digits from 2 to 9 (inclusive), return all the possible letter combinations that the number could denote. The resultant list should be sorted lexicographically.</p>
<p>The digits map to different letters as shown in the below image:</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/phone-combinations.png" />
<h5>Example</h5>
<pre class="plaintext hljs"><code>String: 234
Combinations: [
    "adg", "adh", "adi",
    "aeg", "aeh", "aei",
    "afg", "afh", "afi",
    "bdg", "bdh", "bdi",
    "beg", "beh", "bei",
    "bfg", "bfh", "bfi",
    "cdg", "cdh", "cdi",
    "ceg", "ceh", "cei",
    "cfg", "cfh", "cfi"
]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’, denoting the number of test cases.</p>
<p>For each test case, the input has a string denoting the phone number.</p>
<h4>Output Format</h4>
<p>For each test case, the output has the following lines:</p>
<ul>
<li>The first line contains an integer ‘m’ denoting the total no of combinations.</li>
<li>The next line contains m space-separated strings denoting elements in that particular combination.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
2
23
234</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
a b c
9
ad ae af bd be bf cd ce cf
27
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>'2' &lt;= digit &lt;= '9'</code></p>
<p><code>1 &lt;= length &lt;= 4</code></p>

---
# [Solution](solution.md)
