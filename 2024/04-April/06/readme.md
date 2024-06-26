# 06 Apr 2024

# Questions

---
## [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)

<div class="elfjS" data-track-load="description_content"><p>Given a string <font face="monospace">s</font> of <code>'('</code> , <code>')'</code> and lowercase English characters.</p>
<p>Your task is to remove the minimum number of parentheses ( <code>'('</code> or <code>')'</code>, in any positions ) so that the resulting <em>parentheses string</em> is valid and return <strong>any</strong> valid string.</p>
<p>Formally, a <em>parentheses string</em> is valid if and only if:</p>
<ul>
<li>It is the empty string, contains only lowercase characters, or</li>
<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "lee(t(c)o)de)"
	<strong>Output:</strong> "lee(t(c)o)de"
	<strong>Explanation:</strong> "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
	</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a)b(c)d"
	<strong>Output:</strong> "ab(c)d"
	</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "))(("
	<strong>Output:</strong> ""
	<strong>Explanation:</strong> An empty string is also valid.
	</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
<li><code>s[i]</code> is either<code>'('</code> , <code>')'</code>, or lowercase English letter<code>.</code></li>
</ul>
</div>

---
# [Solution](solution.md)