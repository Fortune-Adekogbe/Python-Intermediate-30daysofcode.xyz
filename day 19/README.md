# Sorted IndEx
 
 
### Task 1: Insertion Sort

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands. Write a function named insertion that takes in a list of integers or strings (never a combination) and returns the sorted list.
Description of the insertion sort algorithm:
Consider the first element to be sorted and the rest to be unsorted. Compare with the second element: If the second element is less than the first element, insert the element in the correct position of the sorted portion. Else, leave it as it is. Repeat the above until all elements are sorted. As is obvious, this should be done in place.
Constraints:
•Use of chr() and ord() are not allowed.
•Use of sorted() or .sort() is disallowed.


### Task 2: Biggie
Given an array of numbers and an index i, write a function named biggie that return the index of the nearest number greater than the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If the distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then raise an error.

Note:
• Raise only AssertionErrors
• No inbuilt modules are allowed 
