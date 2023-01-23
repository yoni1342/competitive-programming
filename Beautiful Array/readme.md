                                                            B. Beautiful Array
                                                            time limit per test2 s.
                                                            memory limit per test256 MB
                                                            inputstandard input
                                                            outputstandard output
Given an array of n
 distinct integers, Haile considers this array beautiful if he can divide this array into three non-empty sets so as the following conditions hold:

The product of the numbers in the first set is less than zero (<0)
.
The product of the numbers in the second set is greater than zero (>0)
.
The product of the numbers in the third set is equal to zero.
Each number from the initial array must occur in exactly one of the sets.
Given a beautiful array help Haile divide the array.

Input
The first line of the input contains integer n
 (3≤n≤100)
. The second line contains n
 space-separated distinct integers a1,a2,…,an
 (|ai|≤103)
, the elements of the array.

Output
In the first line print, n1
 (n1>0)
, the number of elements in the first set. Then print n1
 numbers, the elements in the first set.

In the second line print, n2
 (n2>0)
, the number of elements in the second set. Then print n2
 numbers, the elements in the second set.

In the third line print, n3
 (n3>0)
, the number of elements in the third set. Then print n3
 numbers, the elements in the third set.

The printed sets must meet the specified requirements. It is certain that a solution exists. If there are multiple solutions, you may print any of them.

Examples
inputCopy
3
-1 2 0
outputCopy
1 -1
1 2
1 0
inputCopy
4
-1 -2 -3 0
outputCopy
1 -1
2 -3 -2
1 0
