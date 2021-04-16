# Bell numbers
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 020, is a problem recently posed by Microsoft:

Bell numbers are useful for counting the possible partitions of a set.
EX.
let's say we have 2 numbers in the set :
{1, 2} : {{1}, {2}}, {{1, 2}} => 2 ways
Let's say we have 3 numbers in the set :
{1, 2, 3} : {{1}, {2}, {3}}, {{1, 2, 3}}, {{1, 2}, 3}}, {{2, 3}, {1}}, {{1, 3}, {2}} => 5 ways
# -----------------------------------------------
Defining bell number : B(n) = sigma(S(n, k)) from i = 0 to k
Now, defined recursively : S(n+1, k) = k*S(n, k) + S(n, k-1)
Naive solution would be compute all bell numbers from 1 to n, from i = 0 to K and sum up all the values for getting nth bell number.
Can we do better ? especially for range queries ?
Yes, we can use BELL triangle and compute it using DP.
how do we build the bell triangle :


    1
    1 2
    2 3 5
    5 7 10 15
   15 20 27 37 52
    ...............
Hence, we observe that,
while filling it till i == j:
if j == 0 (first column), we copy the last rows last value : Bell(i, j) = Bell(i-1, i-1)
else: we add up last two values from last column and upper row,: Bell(i, j) = Bell(i-1, j-1) + Bell(i, j-1)

# --------------------------------------------------
APPLICATIONS :
 * BELL NUMBERS => 1, 1, 2, 5, 15, 52, 203, 877, 4140.....
 * counting the number of ways a set can be partitioned
 * If a number N is a squarefree positive integer (meaning that it is the product of some number n of distinct prime numbers),
 then Bn gives the number of different multiplicative partitions of N.
 * The Bell numbers also count the rhyme schemes of an n-line poem or stanza.
 An example of the ABAB rhyming scheme, from "To Anthea, who may Command him Anything", by Robert Herrick:
 Bid me to weep, and I will weep		A
 While I have eyes to see		B
 And having none, yet I will keep		A
 A heart to weep for thee		B
 Thus, the 15 possible four-line rhyme schemes are AAAA, AAAB, AABA, AABB, AABC, ABAA, ABAB, ABAC, ABBA, ABBB, ABBC, ABCA, ABCB, ABCC, and ABCD.
 
# ---------------------------------------------------


## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).