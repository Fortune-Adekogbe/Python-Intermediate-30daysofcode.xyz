<h1>DAY25: MAGIC METHODS</h1>

 

<p>Magic methods or overloaded operators are a way of using normal arithmetic or Boolean operators to perform unique operations on objects of classes we have created.</p>

 

<h2>TASK</h2>

<p>Create a Vector class.<br>

Every Vector has an x,y and z co-ordinate.<br>

Create a Vector constructor that takes in 3 integers, the x,y and z coordinates and initializes their values.
</p>
 
<p>
Create a function info() within the class that RETURNS the vector information as a string in the following form

<pre>'xi+yj+zk'</pre>

where x,y,and z have their usual meanings
</p>
 

<p>create a function magnitude() also within the class that calculates the magnitude of the vector and RETURNS its value to 2 decimal places.</p>

 

 

<p>Overload the following operators</p>
<pre>
(+): Given two vector objects A  and B  the result of A+B should be a new vector object with x,y and z value <br>equal to the sum of that of A and B
<br>
(-): Given two vector objects A  and B  the result of A-B should be a new vector object with x,y and z value <br>equal to that of A –B.
<br>
(*): Given a vector object and a scalar(integer)  it should return a vector object with x,y and equal to the scalar  multiplied by the x,y and z coordinates of the original vector

Given 2 vector objects It should return the scalar product of the vectors

(**): Given two vector objects it should return their cross product which is a new vector object

(==): Compares two vectors to determine if they are equal in magnitude. Returns True or False
</pre>
 

<h2>SAMPLE</h2>
<pre>
A=Vector(2,-5,7)

B=Vector(1,2,3)

B.info() #returns "1i+2j+3k"

A.info() #returns '2i-5j+7k'

C=A+B

C.info() #returns '3i-3j+10k'

D=A-B

D.info() #returns '-1i+7j-4k'

E=A*2

E.info() # returns '4i-10j+14k' 

F=A*B #does the dot product 

F=13

G=A**B #does the cross product

G.info() #returns '-29i+1j+9k'

H=Vector(3,2,1)

H==A #returns True
</pre>
 

<h2>NOTE</h2>
<pre>
•Only assertion errors should be raised if need be

•Do not import any modules
</pre>
