# Sort_transformed_array_or_square
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 032, is a problem recently posed by Microsoft:

Program taking input of sorted list of negative and positive numbers, and we need to
give the output: squares of numbers in the sorted order.

So, first of all, what is the form of output we need to return ? so, let's assume we can
return a newly created list of sorted squares of the input list.
Naive approach would be to simply square the numbers and apply in-built sort ,
that will take time : 0(N*lg(N)) with 0(1) space.
##### Can we optimize it more ?
We can square the numbers up and then use Counting sort on this array.
##### This will take, time : 0(N), space : 0(max(arr)).
Now, can we optimize it further in terms of space efficiency ?
So, we need to observe and use the inherent property that given array is already sorted.
So, we can simply think about a partition, which can divide the array into positive and
##### negative parts of array.
Then, we can apply merge procedure for two sorted parts - one contaning all of positive
and one contaning all of negative.
##### This will Take TIME : 0(N), SPACE : 0(N), N IS SIZE OF ARRAY.

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).