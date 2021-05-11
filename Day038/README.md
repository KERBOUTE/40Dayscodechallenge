# Build_balanced_tree_array
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 038, is a problem recently posed by Apple:

Program for building balanced tree from the given array.
##### IDEA: If we create a tree directly using the arrays elements, then mostly it will be
sweked, and to make it balanced, we need to think in terms of log(N).
so, we can actually apply DAC approach by computing the mid point and making it rootand then recursively build from calling left sub tree and then buuilding from calling right sub tree.
We can take example for follwoing tree and visualize stack call :
let's take , arr = [1, 2, 3, 4, 5, 6, 7]

So, mid is 4, then we go for building left subtree (1, 2, 3) and right subtree (5, 6, 7) with 4 as root.

Then, mid is 2 and we create the tree with 2 as root , left subtree (1) and rightsubtree (3)

Then, we return to the root - "2" and then we return to root "4", now, we call right side of root "4".

Now, mid is 6 with 6 as root, left subtree (5) and right subtree (7).

Finally, we retunr again to root "6" and then to root "4".

Finally, we return this root as now start > end.

```
# --------------------------------
# BFS FOR ABOVE TREE WOULD LEAD TO  : 4 2 6 1 3 5 7
#                     4
#                   /  \
#                  2    6
#                /  \  /  \
#               1   3  5   7
# --------------------------------------
```
## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).