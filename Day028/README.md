# Z algorithm
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 026, is a problem recently posed by Google:

Program to flatten multi level linked list so that first level comes first, second level comes second, third level comes third
and so on in order of their linkage

IDEA: We can clearly observe that we need to process one by one every node and check if it has a child, then process their child and then check again....
optimised Logic is to traverse over each node and if it has a child, then append it's starting head to the end of the previous level (first level) of the list so that all others following it will be automatically in order added, now we also need to keep a tail pointer so that addition of these element is done in 0(1) time and then, we just update this tail pointer to that last node of child's level traversal.
so that next time, we start traversing and keep on checking for every node in this way.
TIME : 0(N), BECAUSE WE PROCESS ONE NODE ALL ONCE, SPACE : EXTRA SPACE NEEDED FOR TAIL POINTER AND ONE TEMP POINTER


[10] -> [5] -> [12] -> [7] -> 11                      
|                       |                                
[4] -> [20] -> [13]    [17] -> [6]                    
        |       |       |                          
       [2]     [16]    [9] -> [8]
                 |      |
               [3]     [19] -> [15]

----------------------------------------------------

10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 
 ^                                      ^
10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 
      ^                                 ^
10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 
            ^                           ^
10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 ->         => 10 -> 5 -> 12 -> 7 -> 11 -> 4 -> 20 -> 13 -> 17 -> 6 ->  [second level completely merged into first level]
                  ^                      ^                                ^
Similarly, for other levels.
 -----------------------------------------------------

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).