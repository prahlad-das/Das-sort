# Das-sort
Fastest sorting algorithm for integers. Order O(n)

Limitations:
* It can be used only for sorting integers.
* It is more efficient when value of integers in the list is not high. 

To start with, we create an empty list to store sorted integers. Now, we go throgh the integers in the original list one by one. Assume our original list is [5,8,9,10,1,2,7]. Now, we take first integer and place it at fifth index in our newly created list. As the new list is empty, so we will place empty string at the other indices. So now, our new list will look like this ['','','','','',[5]]. When we enter integer at particular index, we enter it as a sublist, so that if there is any duplicate integer, we can add that to particular index in sublist. After entering all the integers, our new list will look like this. ['',[1],[2],'','',[5],'',[7],[8],[9],[10]].


This is fine when integers are non-negative. Now how to handle negative integers? For that, we insert negative integers towards left hand side just like as they appear on number line. But now our first integers in the list is no longer 0. To keep track of where our 0 is, we store the number of integers before zero in a separate variable offset. For example, our unsorted list is [-4, 3, 5, -1, 0], then new list will be [[-4], '', '', [-1], [0], '', '', [3], '', [5]]. Now we iterate through new list and combine all the sublists removing empty strings which will give us sorted list [-4, -1, 0, 3, 5]. 

















