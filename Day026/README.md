# Z algorithm
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 026, is a problem recently posed by Google:


Idea is based on KMP algorithm but more efficent.
 
This algorithm basically precomputes called as "Z-values" in a array.
This array values basically tells us that every value indicates that is the longest substring matching
starting from that index where we check that value.
Now, the important trick is that, we actualy compute this z array for the string made by concatenating
the original string and pattern string and grouped using a special symbol separating them "$".
Hence, overall string for which this z-array is calculated : Pattern+'$'+Text.
After calculating the z array, we traverse the entire array and if at anytime we encounter value equal to
length of pattern, then it means we found the pattern in the string (Text).
And finding the index of occurence : would be idx where this value is found - len(pattern) - 1.

The main trick is in computing this Z-array in linear time.

Let's see the example for Z -array :

a b a $ a b a b

[0 0 1 0 3 0 2 0]

As can be seen, at every index, like index "4" is value 3, starting from there 3 is longest matching "abc".
This is a good trick which we apply after concatenating Text and pattern into a single string and apply
this algorithm and computes all z array values.

TIME : 0(M + N), M, N IS LENGTH OF TEXT AND PATTERN RESPECTIVELY.
SPACE : 0(M + N)

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).