
# S² & S²


### Task 1: Selection Sort
Write a function named selection that takes in a list as input and returns the sorted version of the list. In selection sort we are continuously grabbing the smallest unsorted element and placing it in a sorted order in a new array. This process continues iteratively until the list is fully sorted. Implement this without creating a new list to store your sorted items.
Example:
selection([3,2,1,4]) returns [1,2,3,4]

Constraints:
Do not use the min() or max() functions.

### Task 2: Shortest Substring

Given a string and a set of characters write a function named short_sub that return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
Thus, short_sub("structure",{'t','u'}) should return "tu"
If there is no substring containing all the characters in the set, raise an error. Also assume that there will be only one shortest sub string.
For example: short_sub('wednesday',{'d' 'e','f'}) triggers an error.

Note:
•The sort and sorted() functions should not be used

••No inbuilt modules are allowed

•••Only AssertionErrors should be raised
