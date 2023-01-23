C. Beautiful Chess
time limit per test1 s.
memory limit per test256 MB
inputstandard input
outputstandard output
Süha has an 8×8
 chessboard whose rows are numbered from 1
 to 8
 from top to bottom and whose columns are numbered from 1
 to 8
 from left to right.

Süha has placed exactly one bishop on the chessboard. The bishop is not placed on the edges of the board. (In other words, the row and column of the bishop are between 2
 and 7
, inclusive.)

The bishop attacks in all directions diagonally, and there is no limit to the distance which the bishop can attack. Note that the cell on which the bishop is placed is also considered attacked.

<img class="tex-graphics" src="https://espresso.codeforces.com/6209f43aa5d38a9ba43e8c4db93aa9f3bf50b423.png" style="max-width: 100.0%;max-height: 100.0%;">
An example of a bishop on a chessboard. The squares it attacks are marked in red.
Süha has marked all squares the bishop attacks, but forgot where the bishop was! Help Süha find the position of the bishop.

Input
The first line of the input contains a single integer t
 (1≤t≤36
) — the number of test cases. The description of test cases follows. There is an empty line before each test case.

Each test case consists of 8
 lines, each containing 8
 characters. Each of these characters is either '#' or '.', denoting a square under attack and a square not under attack, respectively.

Output
For each test case, output two numbers row
 and col
 (2≤row,col≤7
) — the row and column of the position of the bishop.

It is always guaranteed there is only one bishop which is not place on the edge of the board.

Example
inputCopy
3

.....#..
#...#...
.#.#....
..#.....
.#.#....
#...#...
.....#..
......#.

#.#.....
.#......
#.#.....
...#....
....#...
.....#..
......#.
.......#

.#.....#
..#...#.
...#.#..
....#...
...#.#..
..#...#.
.#.....#
#.......
outputCopy
4 3
2 2
4 5
Note
The first test case is pictured in the statement. Since the bishop lies in the intersection row 4
 and column 3
, the correct output is 4 3.

