# SECURE THE BAG

You're playing a game on a 2D plane and you're to create a function that helps your videogame character find the shortest path to where the loot is on the plane given that there are obstacles along the way.
Write a function named pathfinder that takes in the 2D plane a matrix represented as a list of lists, a tuple containing coordinates of the start point and a tuple containing coordinates of the destination. The function returns an integer representing the lowest number of steps required to reach the destination.

The 2D plane will be a matrix of zeroes and ones where 1s are pathways and 0s are obstacles. Raise an error if there is no pathway. Standing on obstacles is disallowed.

For example:
If
<pre>matrix = [
          [1, 0, 1, 1],
          [1, 0, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0]]
pathfinder(matrix,(0,0),(0,3))==7</pre>
And If:
<pre>matrix2 =  [
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1]]
pathfinder(matrix2,(2,3),(3,7))==7
pathfinder(matrix2,(0,2),(8,8)) raises an error.</pre>

### Note:
<pre>No inbuilt module should be used 
Only AssertionErrors should be raised</pre>
