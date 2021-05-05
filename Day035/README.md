# Merge_two_sorted_arrays
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 035, is a problem recently posed by Amazon:

program to merge two sorted array together and return the sorted array
#### Method 1 efficient is to simply create a additional third array to keep the sorted elements, now create three pointers each one for all three arrays,
now, check whichever is small, copy that element in the third array and then simply increment that array's pointer , similarly when one of the
pointer exhausts due to array size, start simply copying them one by one as they are already sorted within themselves.
##### time : 0(m + n)
##### space : 0(m + n)

#### Method 2 focuses on without using any additional space
idea is to simply pick the elementes one by one from last of second array, and start traversing from last of first array
and then, keep on shifting the elements right one by one until we found a postion for second elemetn in the first array,
in which case then, we have to swap the elements in both arrays, threby maintaining sorted order.
##### time : 0(m*n)
##### space : 0(1)

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).