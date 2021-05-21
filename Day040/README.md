# Word_ladder
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 040, is a problem recently posed by Facebook:

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.

Each transformed word must exist in the word list.

##### Note:
Return 0 if there is no such transformation sequence.

All words have the same length.

All words contain only lowercase alphabetic characters.

You may assume no duplicates in the word list.

You may assume beginWord and endWord are non-empty and are not the same.

##### Example 1:
```
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
#           *OT 
#         / 
#   HOT : -- H*T
#         \ 
#           HO*
#
# HIT -> COG, WE ALL HAVE POSSIBLE CHOICES FROM a - z to choose from.
#
# hit -> hot -> dot -> lot -> dog
# so, output : 5
# Output: 5
```
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

##### Example 2:
```
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
```
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

This problem can be formulated as a graph if we can represent all the word list along with start and end word as graph.
Now, we need to actually find the shortest length of transformation so, BFS in the graph traversal will surely give us the shortest length of chain of transformations.

##### TIME : 0((M ^ 2) * N), where M is the length of each word and N is the total number of words in the input word list.
##### SPACE : 0((M ^ 2) * N)

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).