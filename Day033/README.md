# Alien_dictionary_order
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 033, is a problem recently posed by Apple:

Alien uses the some alien language using the same 'a-z' letters but the order of those chars can maybe or maybe not different than we use.
Program for finding the order of letters, given Sorted dictionary of words in that alien language.
#### Examples:

###### Input:  
words[] = {"baa", "abcd", "abca", "cab", "cad"}
###### Output: 
Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

##### Input:  
words[] = {"caa", "aaa", "aab"}
##### Output: 
Order of characters is 'c', 'a', 'b'

We need to first understand that in the normal dictionary, how do we get the order of letters ?
let's say :
```
cat   ---   
        | =>  we know cat comes before dog as 'c' comes before 'd' 
dog   ---
```
matching same chars in both strings will not be beneficial as we can't get any info from it, but if there are unmatching chars in the string, then it can be good, 
we are able to find the order of chars/letters using the first unmatched char in both the strings.
Similarly, we can do for this alien language, since we know it's sorted in the order, so if any unmatched char comes before unmatched char in the second string, 
then, it means we have got some order.
similarly, go for all the words and get the order of all the letters.

```
#               a -> c
#               -------
#              |      |
# baa | abcd | abca | cab | cad
# ^     ^  ^      ^     ^     ^
# |     |  |      |     |     |
# -------   -------      ------
#   |          |            
#  b  -> a   d -> a       b -> d
```

So, there are 4 important info  : [b -> a, d -> a, a -> c, b -> d]
Now, if we observe carefully, then this can be represented as a graph of directed edges of all unmatched chars pairs from all words.
Then, we can perform "topological sorting", to perform the relative ordering of all chars.
As, we can get the ordering of any pair of chars by using only DFS but we need to get relative ordering of all chars of pairs, hence, we need topological sorting.

#### TIME : 
0(N * max_size_of_word) + 0(E + V), N is total words in the array, max_size_of_word is maximum size of all the possible words in the dict, E, V are edges and nodes  of graph.

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).