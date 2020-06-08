# Day 8: Back to base

Write a function named to_base that converts a number in **base 10** to its **Binary(2)**, **Quatenary(4)**, **Octal(8)** or **Hexadecimal(16)** versions. 

The function should take in a **decimal integer** and the **desired base(in integer form)** as parameters and return the converted number as a string.

##### Quite easy yeah?

 

### Constraints: 

•Do it without using the **`division(/)`**, **`modulus(%)`** and **`floor division(//)`** operators.
<br>
•Do not use the **bin()** or **hex()** functions.
<br>
•Do not import any modules.
<br>
•Only raise AssertionErrors if need be.
<br>
•Hexadecimals should be in lowercase.
<br>
## Examples:
<pre>
to_base(3,2)=='11'

to_base(432,4)=='12300'

to_base(64,8)=='100'

to_base(249,16)=='f9'
</pre>
 

### Hints: 

•Use Bitwise Operators
<br>
•All the bases listed are powers of 2
