
# 30 May 2023

# Questions

---
## [1. Implement Queue using Stacks](https://workat.tech/problem-solving/practice/implement-queue-using-stacks) [(LeetCode)](https://leetcode.com/problems/implement-queue-using-stacks/) 

<p>Implement a queue using one or more stacks.</p>
<p>The Queue class should support the following methods:</p>
<ul>
<li>int size()</li>
<li>boolean isEmpty()</li>
<li>int front()</li>
<li>int back()</li>
<li>void push(int element)</li>
<li>void pop()</li>
</ul>
<p>You can assume that you've access to a Stack class which provides the following methods:</p>
<ul>
<li>int size()</li>
<li>boolean isEmpty()</li>
<li>int top()</li>
<li>void push(int element)</li>
<li>void pop()</li>
</ul>
<h4>Main method:</h4>
<ul>
<li>Queue created of size 10</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
<li>Pushed: 5</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
<li>Pushed: 6</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
<li>Pushed: 7</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
<li>Popped</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
<li>Popped</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
<li>Popped</li>
<li>Printed: queue.front() queue.back() queue.isEmpty() queue.size()</li>
</ul>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>-1 -1 true 0
5 5 false 1
5 6 false 2
5 7 false 3
6 7 false 2
7 7 false 1
-1 -1 true 0</code></pre>

---
## [2. Implement Stack using Queues](https://workat.tech/problem-solving/practice/implement-stack-using-queues) [(LeetCode)](https://leetcode.com/problems/implement-stack-using-queues/) 

<p>Implement a stack using one or more queues.</p>
<p>The Stack class should support the following methods:</p>
<ul>
<li>int size()</li>
<li>boolean isEmpty()</li>
<li>int top()</li>
<li>void push(int element)</li>
<li>void pop()</li>
</ul>
<p>You can assume that you've access to a Queue class which provides the following methods:</p>
<ul>
<li>int size()</li>
<li>boolean isEmpty()</li>
<li>int front()</li>
<li>int back()</li>
<li>void push(int element)</li>
<li>void pop()</li>
</ul>
<h4>Main method:</h4>
<ul>
<li>Stack created of size 10</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
<li>Pushed: 5</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
<li>Pushed: 6</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
<li>Pushed: 7</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
<li>Popped</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
<li>Popped</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
<li>Popped</li>
<li>Printed: stack.top() stack.isEmpty() stack.size()</li>
</ul>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>-1 true 0
5 false 1
6 false 2
7 false 3
6 false 2
5 false 1
-1 true 0</code></pre>

---
# [Solution](solution.md)
