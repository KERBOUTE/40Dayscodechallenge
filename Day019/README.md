# Program for bit efficient arrays
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 016, is a problem recently posed by Airbnb:

Since, array elements can take upto 32 bits (assuming 32 bit machine) for just one int num
but we actually need just one bit to represent the int num, so in just one index of arr
that is one bucket of array, we can actually store information for 32 int by setting the
particular bit of that int num and same can be done for checking the set bits.
So, we can get actually which bucket the int goes is given by pos / 32 (pos >> 32)
and now, which actual bit pos to set or test is given by pos % 32 (as total 32 bits : 0...31)
So, we can get the mask to set the num, by left shifting k bits for initial flag = "1",
and ORing this with arr[index] will set the bit at pos.
Also a good way to get modulus of 32 is also by ANDing by 0x1F.
Potential applications would include but not limited to finding duplicates in the array in very
efficient way.


## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).