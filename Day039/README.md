# Convert_binary_tree_linkedlist
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 039, is a problem recently posed by Facebook:

Program for converting binary tree into flattened linked list
```
# -----------------------------------------------------------------------------
# One of the key things is to visualize following diagram in mind :
#
#               1                    1              1
#              /\                   / \              \
#             2  5            =>   2   5     =>        2
#            /\   \                 \   \               \
#           3 4    6                 3   6                3
#                                     \                    \
#                                      4                     4
#                                                              \
#                                                               5
#                                                                \
#                                                                 6
# ----------------------------------------------------------------------------
```
If we think about the above process, it will be easily done with firstly checking if left leaf is not None, then we need to move left part of the tree to its right part for that particular root node.

this should be done recursively for every node in the tree and it will be flattened.

##### TIME : 0(N)

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).