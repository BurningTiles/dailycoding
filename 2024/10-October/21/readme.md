# 21 Oct 2024

# Questions

---
## [1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings)

<div class="elfjS" data-track-load="description_content"><p>Given a string <code>s</code><var>,</var> return <em>the maximum number of unique substrings that the given string can be split into</em>.</p>
<p>You can split string <code>s</code> into any list of <strong>non-empty substrings</strong>, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are <strong>unique</strong>.</p>
<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ababccc"
	<strong>Output:</strong> 5
	<strong>Explanation</strong>: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
	</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aba"
	<strong>Output:</strong> 2
	<strong>Explanation</strong>: One way to split maximally is ['a', 'ba'].
	</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "aa"
	<strong>Output:</strong> 1
	<strong>Explanation</strong>: It is impossible to split the string any further.
	</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li>
<p><code>1 &lt;= s.length &lt;= 16</code></p>
</li>
<li>
<p><code>s</code> contains only lower case English letters.</p>
</li>
</ul>
</div>

---
# [Solution](solution.md)