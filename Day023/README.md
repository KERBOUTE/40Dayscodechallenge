# binary_level_by_level_print
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 023, is a problem recently posed by Amazon:
Program to print level by level order traversal each levels on a new line , for the binary tree.
# -----------------------------------------------------------------
APPROACH : One way to approach is to store a pair of (node, level) info in BFS queue,
and when we insert new children, we increase their level by 1 (by seeing their parent level), similarly
when we pop, again we check if their is any transition from last popped with current popped item
in terms of level, then we know this is the new level.
# ----------------------------------------------------------------
Now, Second approach would be to use a "None" value, whenever we encounter a already None value while
popping out, also on the start we push root and None both so that next time we would enounter None and know that
we have crossed first level, similarly, whenerv we encounter None while popping out, we push another None,
while the stack is not empty, if at any time stack is empty after popping, we stop.
# ----------------------------------------------------------
# EXAMPLE  :
                        8           8
                       /   \
                     10     3        10, 3
                    /  \     \
                    1   6      14    1, 6, 14
                        /\      /
                       9  7   13     9, 7, 13
# ----------------------------------------------------------------
TIME : 0(N), SPACE : 0(W), W IS WIDTH OF BINARY TREE.

# Used the second approach

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).