# Spiral_traversal_matrix
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 031, is a problem recently posed by Facebook:

Program for printing the matrix in spiral form , that means one by one square loops going one by one inside one of each other
#### IDEA: logic is very simple, we need to set four boundaries so that we can print one by one all of the four sides of the square loop for each loops
for that we set : k, l, m, n -> where k is used to set boundary for first row (from left to right),n is used to set last column boundary (from top to bottom), m is used to set boundary for last row (from right to left), l is used to set boundary for first column (from bottom to top)
In this way we go from first row   ->  last column   ->   last row   ->   first column in clockwise direction (spiral way) 
Now, going for innner loops, from observation we can see that , k   ->   incremented, n-> decremented, m -> decremented, l-> incremented
#### TIME : 0(M*N) WHERE M, N -> ROWS, COLUMNS AND SPACE : 0(1)
WE CAN VISUALIZE THE ALGORITHM AS SHOWN BELOW USING FOUR POINTERS : 

```
# TOP ->  [1, 2, 3, 4]
#         [5, 6, 7, 8]
#         [9, 2, 4, 1]
# BOTTOM->[5, 4, 1, 1]
#          ^        ^
#         LEFT     RIGHT    
```
TOP TO BOTTOM => CONTROLS ROWS

LEFT TO RIGHT => CONTROLS COLS

So, let's say we print first row, so, we run loop from left to right, and since top should be constant, then print a[top][col], col is going From left to right.
Similary, for other three segments, last col, last row, then finally first row.
Alternate way :  we can run the above logic using "Dir" variable which can increment every time we run inside while loop, dir = (dir + 1) % 4
Which will be cyclic as we want, 0, 1, 2, 3, 0, 1, 2, 3... And associate all four numbers with respective ordering or direction.

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).