# DAY 26

## Merge Sort:
Follow [this link](https://docs.google.com/document/d/1EtsyyTu4uzEqTtLcEUivCi8lgZP4U5UVg9i_9tEnD0o/edit?usp=drivesdk) to view the task  


## My Pal:

Given a string s, write a function named **`long_pal`** to find the **longest palindromic substring in s**. 
You may assume that the maximum length of s is 1000. 
**If there is no palindrome, return None.**

<pre>
string = "babad"

long_pal(string)= "bab". Note: "aba" is also a valid answer.

Example 2:

long_pal( "cbbd" ) returns "bb"
</pre>

## Chances:

Given the number of faces on a dice(f), the number of dices thrown(d), the desired number(n) and the desired range of occurrence(oc),  
write a function named **`probability`** that returns the probability of n facing up on the dices oc times.  
  
###Constraints:
5<f<9  
1<d<20  
0<n<=f  
oc is  a range(a,b)   
<br>
a: minimum number of occurrence
<br>
b: maximum number of occurrences 

### EXAMPLE:
<pre>
probability(6,2,6,range(1,3))==0.3056

probability(6,3,6,range(1,4))==0.4216

probability(8,4,6,range(0,5))==1.0
</pre>

## NOTE:
  
No inbuilt modules are allowed 
