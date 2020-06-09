What 2-Do 2-D 2-D ARRAY
 

<h2>1. ROTATE THE 2-D ARRAY</h2>

 
<p>
Write a function rotate which when given a square 2-D array of integers rotates the array 90° clockwisely
<br>
Don't  create an additional array
<br>
e.g</p>
<pre>
if arr=

[[1,2,3],

 [4,5,6],

 [7,8,9]]

 

then rotate(arr) should change the array to 

[[7,4,1],

 [8,5,2],

 [9,6,3]]

<strong>Note It does not return a new matrix. It changes the elements in the original matrix.</strong>
</pre>
 

<h2>2. READ THE 2-D ARRAY</h2>

 
<p>
Write a function loop_read which when Given a 2D array , RETURNS a string containing all the elements starting from top left element and going in a round loop.
<br>
The array will either be an array of integers or strings.
<br>
e.g </p>
<pre>
if arr=

[[1,   2,   3,  4],

[12,  13,  14,  5],

[11, 16,   15,  6]

[10,  9,   8,   7]]

loop_read(arr)  should return 

"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"

 

if arr=

[[ 1,  2,  3,  4,  5],

 [12, 13, 14, 15, 6],

 [11, 10, 9,  8,  7]]       

loop_read(arr) will return

"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"

<strong>As shown in this example, the array will not always be  a square matrix.<strong>
</pre>
 

<h2>NOTE</h2>
<pre>
<ul>
<li>Only AssertionErrors should be raised if need be</li>
<li>Do not import any modules.</li>
</ul>
</pre>
