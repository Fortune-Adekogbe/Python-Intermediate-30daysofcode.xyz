<h1>Q<-UEUES</h1>
 
<p>
Classes ✅ check<br>

Linked list ✅ check<br>

 

That's good cos you'll need them for today's task.
</p>
 
<p>
A <strong>Queue</strong> is a data structure that follows the first in first out (FIFO) order. <br>Just as the name describes it is similar to a queue of people at an atm stand. The first person to get there will be the first to leave (in a normal place)

 

You will be implementing  a <strong>Queue</strong> using <strong>Linked lists</strong> in this Task.
</p>
 

<h2>TASK</h2>
 

<p>create a <strong>Node class</strong>
<br>
Each node has a <strong>value (integer)</strong> and a <strong>next (Type Node</strong> that it's pointing to
<br>
 

Create a constructor that takes in an integer and initializes the value variable to the integer
<br>
value should be accessible as self.value
<br>
next should be available as self.next
<br><br>
implement a <strong>Queue class</strong> 

a <strong>Queue</strong> has a parameter <strong>head(Type Node)</strong>. Initial value of head=None. 

 

The constructor for <strong>Queue</strong> doesn't take any parameters.

 

implement an <strong>enqueue()</strong> method which takes a <bold>value(integer)</bold> and pushes(appends)<br> it to the end of the <strong>Queue</strong>.

 

implement a method <strong>dequeue()</strong> which removes the element in the front of the <strong>Queue</strong>. <br>and RETURNS the value of that element.

If the Queue is empty raise AssertionError. 

 
<br>
implement a method <strong>front()</strong> which RETURNS the value of the element in front of the <strong>Queue</strong>.<br> If the <strong>Queue</strong> is empty it returns None

 

implement a ,strong>count()</strong> method which RETURNS  the number of elements in the <strong>Queue</strong>

 

<strong>Note that each member in the queue is of type Node</strong>

<strong>Needless to say all the functions are inside the Queue class</strong>
</p>
 

<h2>Sample case</h2>
<pre>
my_queue=Queue()

The Queue is empty and only head(None) is present

The Queue is 

None

my_queue.front()    #returns None

 

my_queue.enqueue(8)

my_queue.enqueue(10)

my_queue.enqueue(23)

my_queue.enqueue(4)

my_queue.enqueue(13)

my_queue.enqueue(45)

The Queue becomes 

8-->10-->23-->4-->13-->45-->None



my_queue.front()  #returns 8

Note that each of the members of the queue are of type Node and only their value is shown there.
 
 
my_queue.dequeue()#returns 8

my_queue.dequeue()#returns 10

my_queue.dequeue()#returns  23
 
The Queue become

 

4-->13-->45-->None


my_queue.count()#returns 3

my_queue.front()#returns 4

 </pre>
 

 

•Only Assertion Errors should be RAISED if need be

 

•NO BUILT IN MODULES SHOULD BE USED

