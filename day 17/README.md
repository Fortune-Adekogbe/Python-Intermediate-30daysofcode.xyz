<h1>Day 17</h1>

<h2>Task 1: <bold>K</bold>ombinatio<bold>N</bold></h2>

<p>Create a function *combo* that takes a list of N integers and a positive integer K  and returns a list of all combinations of K elements in the list.
<br>
e.g</p>
<pre>
combo([1,2,3],2)= [[1,2],[1,3],[2,3]]

combo([1,2,3,4,5],4)= [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
</pre>

<h2>Task 2: SHARE THE MONEY</h2>

<p><strong>Uncle Geek</strong> comes to visit you and your brother. Before he leaves he leaves some money for you and your brother.<br> Some nice naira notes.

You and your brother decide you will share the money equally.
<br>
Given an array of integers where the integers represent the naira notes Geek gave you guys,
<br>
write a function
my_money() that takes the array of the notes worth and RETURNS a boolean if its possible to share the money into exactly half only with the naira notes Geek gave you.
</p>
<pre>
Example:
a) my_money([5,50,100,10]) returns False

No matter how you split the notes you cant get equal amounts

my_money([1000,500,500]) returns True

This can be split equally as 

[500,500],[1000]

c) my_money([5, 5, 10, 100, 100, 200, 200, 500, 500, 1000])=True
</pre>

<h2>NOTE</h2>
<pre>
•NO BUILT IN MUDULES SHOULD BE USED

•DO NOT IMPORT ITERTOOLS

•Only AssertionErrors should be raised if need be.
</pre>
 

HINT: You might need to use Recursion

