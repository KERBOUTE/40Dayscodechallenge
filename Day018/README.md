# Intersection of Linked Lists
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 016, is a problem recently posed by Apple:

Program to verify if the alien dictionary is given, then if the given list of words are sorted lexigraphically.
The words are sorted lexicographically if and only if adjacent words are. This is because order is transitive: a <= b and b <= c implies a <= c.
To check whether a <= b for two adjacent words a and b, we can find their first difference. 
For example, "applying" and "apples" have a first difference of y vs e. After, we compare these characters to the index in order.

Care must be taken to deal with the blank character effectively. If for example, we are comparing "app" to "apply", this is a first difference of (null) vs "l".
Here is the implemnetation of above intution for algorithm : 
 -----------------------------------------------------------------------------------------------------------------------------------------------
TIME: 0(N), N IS NUMBER OF WORDS IN THE WORD LIST.
SPACE : 0(1)
```


class Solution:

    def compare(self, word1, word2, order_map):
    # fill this in.

    def isAlienSorted(self, words: List[str], order: str) -> bool:
    # fill this in.

```

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).