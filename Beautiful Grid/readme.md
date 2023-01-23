D. Beautiful Grid
time limit per test2 s.
memory limit per test256 MB
inputstandard input
outputstandard output
Tamirat considers a grid beautiful if it remains the same when rotated 0∘
, 90∘
, 180∘
 and 270∘
.

The picture below shows an example of all rotations of a grid.

<img class="tex-graphics" src="https://espresso.codeforces.com/f49275ace84e3caead703c50c0ac74ee0533a408.png" style="max-width: 100.0%;max-height: 100.0%;">

Tamirat is given a square grid with n
 rows and n
 columns. Each cell contains either 0
 or 1
.

In an operation, he can select a cell of the grid and flip it (from 0→1
 or 1→0
). Find the minimum number of operations he needs to make it beautiful.

Input
The first line contains a single integer t
 (1≤t≤100
) , the number of test cases.

The first line of each test case contains a single integer n
 (1≤n≤100
) , the size of the grid.

Then n
 lines follow, each with n
 characters ai,j
 (0≤ai,j≤1
) , the value in each cell.

Output
For each test case output a single integer  — the minimum number of operations needed to make the grid beautiful.

Example
inputCopy
5
3
010
110
010
1
0
5
11100
11011
01011
10011
11000
5
01000
10101
01010
00010
01001
5
11001
00000
11111
10110
01111
outputCopy
1
0
9
7
6
Note
In the first test case, we can perform one operations to make the grid 010111010
. Now, all rotations of the square are the same.

In the second test case, all rotations of the square are already the same, so we don't need any flips.
