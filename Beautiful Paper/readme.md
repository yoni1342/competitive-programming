                                                                    A. Beautiful Paper
                                                                    time limit per test1 s.
                                                                    memory limit per test256 MB
                                                                    inputstandard input
                                                                    outputstandard output
                                                                    
                                                                    
Haile considers a piece of paper to be beautiful if it is square; if a piece of paper is beautiful, he cuts it into two rectangular papers with either a horizontal or vertical cut to avoid being distracted. Now, you see two rectangular papers on his desk and wonder if they were once one square. In other words, check if you can make a square out of the two given rectangles.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of test cases in the input. Then t
 test cases follow.

Each test case is given in two lines.

The first line contains two integers a1
 and b1
 (1≤a1,b1≤100
) — the dimensions of the first one obtained after cutting rectangle. The sizes are given in random order (that is, it is not known which of the numbers is the width, and which of the numbers is the length).

The second line contains two integers a2
 and b2
 (1≤a2,b2≤100
) — the dimensions of the second obtained after cutting rectangle. The sizes are given in random order (that is, it is not known which of the numbers is the width, and which of the numbers is the length).

Output
Print t
 answers, each of which is a string "YES" (in the case of a positive answer) or "NO" (in the case of a negative answer). The letters in words can be printed in any case (upper or lower).

Example
inputCopy
3
2 3
3 1
3 2
1 3
3 3
1 3
outputCopy
Yes
Yes
No
