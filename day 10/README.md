# OOPs

 

Contrary to what the title implies, this task was not a mistake.

**`OOP==Object Oriented Programming`**

 

Create a **class `Student`**.

Every Student has an **`age, weight and height`**

 
Create a constructor that takes in 3 parameters, **a students age,weight and height(<i>in that order</i>)**

and initializes them to those values

 

Create a function **`info()`** which when called by a student object RETURNS a tuple containing **`the age and Body Max Index(BMI)(rounded to 2dp) `** of the student

**`BMI=weight/(height**2)`**

The function **info()** will not take any parameters

 
Lastly create a **`function average()`** which takes a **list of student objects** and RETURNS a tuple containing the average age,weight and height(in that order) of the students in the next 10 years

i.e **10 years from now what would be their average age,weight and height(in that order)**

 

**`Assume that weight increases by 5% each year and height increases by 2% each year.`**

 

## NOTE:

•Age is an integer, weight and height are floats
<br>
•Ensure functions take parameters in the order given.
<br>
•Your float answers should be rounded to 2 dp
<br>
•Only assertion errors should be raised if necessary
<br>
 

e.g

 <pre>

Fortune=Student(23,45.67,7.6)

represents a student whose age is 23, weight is 45.67 and height is 7.6

 

Fortune.info() would return (23,0.79)

 

another student

Joba=Student(22,40.01,8.3)

 

 

average([Fortune,Joba]) would return (32.5,69.78,9.69)

 

e.g for weight in 10 years Joba will weigh 65.17 while Fortune will weigh 74.39 and the average of that is 69.78

</pre>

 

Goodluck. Sorry for the long epistle.
 | 
