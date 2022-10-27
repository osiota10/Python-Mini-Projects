## What is a Bubble Sort?


It is a sorting algorithm that sort a list items in ascending order by comparing two adjacent values. 
In other words, it compares one pair at a time and swaps if the first element is greater than the second element.
If the first element is higher than second element, the first element takes the second element position, while second element takes the first element position. 
If the first element is lower than the second element, then no swapping is done.


## Implementation
Consider the list below, we what to arrange the items in ascending order:

`arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]`


### The solution
Iterate through the list comparing two adjacent elements and swapping them if the first value is higher than the second value.

`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`


### Algorithm
The bubble sort algorithm works as follows

1. Get the total number of elements. Get the total number of items in the given list

2. Determine the number of outer passes `(n – 1)` to be done. Its length is list minus one

3. Perform inner passes `(n – 1)` times for outer pass `1`. Get the first element value and compare it with the second value. If the second value is less than the first value, then swap the positions

4. Repeat step 3 passes until you reach the outer pass `(n – 1)`. Get the next element in the list then repeat the process that was performed in step 3 until all the values have been placed in their correct ascending order.

5. Return the result when all passes have been done. Return the results of the sorted list
