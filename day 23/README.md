# Day 23: Body Count

Remember those images where they'd show some boxes and ask you to count the squares? Yes, the task for today will be something like that.
Given a 2-D matrix represented by a list of lists and an optional parameter thresh which represents the highest order to be considered and has a default value of None, write a function named my_exes that
returnss the number of Xs in the 2-D matrix as an integer.
If thresh is None the total number of Xs from all possibilities should be returned else it represents the maximum dimension to be considered.
The 2-D matrix will consist of 0s and 1s only. All Xs must have every along them as 1.

Below is a first grade X.(thresh==1)

[[1, 1]
[1, 1]]

Below is a second grade X (thresh==2)

[[1, 0, 1],

[0, 1, 0],

[1, 0, 1]]

Note that even if the 0s here were 1s, it will still be considered as an X because it obeys the rule.

Example:
matrix = [

[1, 0, 1],

[0, 1, 1],

[1, 1, 1]]

my_exes(matrix) returns 2

IF matrix[0][1] was set to 1:

my_exes(matrix) returns 3

my_exes(matrix,thresh=1) returns 2

Note:

No inbuilt modules are allowed

Raise only AssertionErrors
