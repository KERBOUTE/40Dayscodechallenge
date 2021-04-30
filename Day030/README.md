# Count_sum_left_leaves
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 011, is a problem recently posed by Amazon:

Program to count and get sum of left leaf nodes in the binary tree.

We can take example for follwoing tree and visualize stack call :
```
#            1
#          /  \
#        2     3
#       /  \
#      4    5
```

We can use any iterative traversal for traversing every node, and check if current.left.left is None and current.left.right is None, then
we include its sum in the overall sum, and we do this for every current.left node.

We can also use recursive approach to solve this , we go for every node, if the root is not None, then check if root.left is leaf node or not ,
if it's leaf node, then we simply add the root.left.data to the res.
Now, if it's the not the leaf node, then we recur for left sub tree. and we every recur for right sub tree.
So, all in all, we recur for both left and right subtrees, but while we go for left, we need to check specifically for leav nodes. That's it.
#### NOTE : HEre, simply recurrence relation like adding left leav(leftsubtree) + right leav(rightsubtree) will not work.
#### TIME : 0(N), SPACE : 0(N).


## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).