	
<h1>DAY 27:</h1>

 

<h2>PERFECT MATCH</h2>

<p>Write a function named match() which when given a list of words, find all indices pairs such that the concatenation of the two words is a palindrome.</p>

<p>e.g</p>
<pre>
match([‘code’,’edoc’,’fedoc’,’doc’,’d’,’ad’]) will RETURN [(0,1),(0,2),(0,3),(1,0),(4,5)]
</pre>
Explanation:
<pre>
‘code’ + ‘edoc’= ’codeedoc’ (0,1)

‘code’+’fedoc’=’codefedoc’ (0,2)

‘code’+’doc’=’codedoc’ (0,3)

‘d’+’ad’=’dad’ (4,5)
</pre>
 

 

<h2>BaLaNcE</h2>

<p>A string of parentheses is said to be balanced if</p>
<ul>
  <li>for every opening parentheses there is a closing parentheses</li>
  <li>the opening parentheses comes before the closing parentheses</li>
</ul>

<p><strong>‘(‘  is an opening parentheses while ‘)’ is a closing parentheses</strong></p>

<p>e.g</p>
<pre>
‘( (  ) ) ) ( ( )’ is not balanced

‘( ( ( ) ( ) ) )’ is balanced
</pre>
 

<p>given a string comprising of opening parentheses, closing parentheses and asterix(*) where * could represent an opening parentheses, closing parentheses or an empty string. Write a function isBalanced() that takes in the string and determines if the string is balanced or not. It RETURNS True if it is Balanced and False otherwise</p>

 

<p>e.g</p>
<pre>
‘( ( ) *’,  ‘( * ) )’  and ‘( * )’ are balanced
</pre>

<pre>In the first the * represents a closing parentheses

In the next one it represents an opening parentheses

In the last it represents an empty string.

isBalanced( ‘) * (‘ ) returns False as no matter what * represents the string in not balanced.
</pre>
 

<h2>NOTE</h2>

<p>•Only assertion errors should be raised if need be</p>

<p>•Do not import any modules</p>
