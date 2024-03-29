                                                                    B. Matrix Rotation
                                                                    time limit per test2 seconds
                                                                    memory limit per test512 megabytes
                                                                    inputstandard input
                                                                    outputstandard output
                                                                    You have a matrix 2×2


filled with distinct integers. You want your matrix to become beautiful. The matrix is beautiful if the following two conditions are satisfied:

in each row, the first element is smaller than the second element;
in each column, the first element is smaller than the second element.

<img class="tex-graphics" src="https://espresso.codeforces.com/42d67912e002442996880308930362fd6a7cafa7.png" style="max-width: 100.0%;max-height: 100.0%;">

You can perform the following operation on the matrix any number of times: rotate it clockwise by 90
 degrees, so the top left element shifts to the top right cell, the top right element shifts to the bottom right cell, and so on:

<img class="tex-graphics" src="https://espresso.codeforces.com/ae24ecc4cb629f9d3369e86a45b651023e45cf29.png" style="max-width: 100.0%;max-height: 100.0%;">

Determine if it is possible to make the matrix beautiful by applying zero or more operations.

Input
The first line contains one integer t
 (1≤t≤1000
) — the number of test cases.

Each test case consists of two lines. Each of those lines contains two integers — the elements of the corresponding row of the matrix. In each matrix, all four elements are distinct integers from 1
 to 100
.

Output
For each test case, print YES if the matrix can become beautiful, or NO otherwise. You may print each letter in any case (YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).

Example
inputCopy
6
1 3
5 7
8 10
3 4
8 10
4 3
6 1
9 2
7 5
4 2
1 2
4 3
outputCopy
YES
YES
NO
YES
YES
NO
