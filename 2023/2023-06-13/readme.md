
# 13 Jun 2023

# Questions

---
## [1. Trailing Zeroes](https://workat.tech/problem-solving/practice/trailing-zeroes) [(LeetCode)](https://leetcode.com/problems/factorial-trailing-zeroes/) 

<p>Given a number, let's say, 102000. Can you count how many zeroes are present at the end of the number?</p>
<p>In this case, it is 3. The zeroes at the end of a number are known as trailing zeroes.</p>
<p>Trailing zeroes are a sequence of zeroes in a number after which there are no other digits.</p>
<h5>Examples</h5>
<p>trailingZeroes(120) &rarr; 1<br/>
trailingZeroes(1300) &rarr; 2<br/>
trailingZeroes(123400) &rarr; 2<br/>
trailingZeroes(1000) &rarr; 3<br/>
trailingZeroes(102000) &rarr; 3</p>
<p>The factorial of a number &lsquo;n&rsquo; is the product of all the numbers from 1 to n.</p>
<h5>Example</h5>
<p>factorial(5) &rarr; 1*2*3*4*5 &rarr; 120<br />
factorial(1) &rarr; 1</p>
<p>Note that factorial(0) is also 1.</p>
<p>Given a number &lsquo;n&rsquo;, find the no of trailing zeroes in the factorial of &lsquo;n&rsquo;.</p>
<p>trailingZeroesInFactorial(10) &rarr; 2</p>
<h3>Testing</h3>
<h4>Input format</h4>
<p>First-line contains &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test-case, the one line containing an integer &lsquo;n&rsquo;.</p>
<h4>Output format</h4>
<p>&lsquo;T&rsquo; lines, each contain the number of trailing zeroes in the factorial of each value of &lsquo;n&rsquo;.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3
5
10</code></pre>
<h4>Expected Output&nbsp;</h4>
<pre class="plaintext hljs" id="expected-output"><code>0
1
2</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 1000</code></p>
<p><code>1 &lt;= n &lt;= 100000</code></p>

---
## [2. Greatest Common Divisor](https://workat.tech/problem-solving/practice/gcd) [(LeetCode)](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) 

<p>The Greatest Common Divisor (GCD) of two or more integers is the largest positive integer that divides each of the integers. For example, the gcd of 8 and 12 is 4.</p>
<p>Here, 8 and 12 both are divisible by 4. There is no number greater than 4 which 8 and 12 are both divisible with.</p>
<h5>Examples</h5>
<p>GCD(2, 4) =&gt; 2</p>
<p>GCD(1, 5) =&gt; 1</p>
<p>GCD(3, 6) =&gt; 3</p>
<p>GCD(4, 12) =&gt; 4</p>
<p>GCD(6, 14) =&gt; 2</p>
<p>Given two numbers, calculate their GCD.</p>

<h3>Testing</h3>
<h4>Input format</h4>
<p>First-line contains &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test-case, one line containing two space-separated integers A and B.</p>
<h4>Output format</h4>
<p>For each test-case, print the gcd of numbers A and B.</p>
<h3>Examples</h3>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4 5
3 6
6 8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
3
2</code></pre>
<h4>Explanation</h4>
<p>For test case 1,
<br/>1 is the greatest number that divides both 4 and 5.</p>
<p>For test case 2,
<br/>3 is the greatest number that divides both 3 and 6.</p>
<p>For test case 3,
<br/>2 is the greatest number that divides both 6 and 8.</p>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= A, B &lt;= 100000</code></p>

---
# [Solution](solution.md)
