# Ternary_search
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 036, is a problem recently posed by Apple:

Sometimes useful to have two midpoints for searching sorted array, which is called ternary search due to two pivot.

```
#       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                 |        |         
#                mid1      mid2
#
#       say we search for "10", 
#       we have three search spaces, from 0....mid1, mid1.....mid2, mid2.....9
#       Like in binary search, we search for three search spaces, and then move to that search space 
#     
#      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                            |      |
#                           mid1   mid2
#
#      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```
now, it matches...... with mid2, index:  "9"
#### TIME : 0(log3(N)), SPACE : 0(1)

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).