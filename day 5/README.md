# WEDDING CHOW  

At the reception of **GeekTutor's wedding**, guests are to be served.  

A complete chow has **```rice(r), stew(s), meat(m), fish(f) and a drink(d).```**

Given a string representing the supplies(chow) available, write a function named **`wedding_chow()`** that takes it as input and RETURNS a **tuple of two elements.**

The **first element is an integer representing the maximum number of guests that can receive complete chow**

and the **second is the left over chow as a string arranged in order (rsmfd)**

**``r,s,m,f and d represent rice, stew, meat, fish and drink respectively.``**

 

<p>Examples</p>:
<pre>
wedding_chow(‘rsmfdrsmfdrsm’) will return (2,'rsm') as it has just 2 complete chows.
</pre>
 
<pre>
wedding_chow(‘fdrsmssrrdr’) will return (1, 'rrrssd') as there is only one complete chow.
</pre>
 

## N/B:
•The strings will not be given in any particular order.

•No inbuilt modules are allowed.

•Note input is case sensitive

•The left over chow should be arranged in order (r,s,m,f,d)

•Only AssertionErrors should be raised.
