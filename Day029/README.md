# hit_counter_design
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 011, is a problem recently posed by Twitter:

Program to design a hit counter.
It should support the following two operations: hit and getHits.

hit(timestamp) – Shows a hit at the given timestamp.
getHits(timestamp) – Returns the number of hits received in the past 5 minutes (300 seconds) (from currentTimestamp).
#### ASSUMPTIONS : 
Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order 
(i.e. the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

### Examples:


HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

### FIRST APPROACH : 
We keep a simple ARRAY, more precisely resiazble array - vector (list), to fill the timestamps as they come in, and then for getting last 5min or 300 seconds, we subtract current timestamp from 300 to get range/duration, now keep moving the index from front till we get inside range.

### SECOND APPROACH : 
Also, now we can observe that too much space is wasted in above solution, because we are keeping non useful elements also in array.
we need to remove these non useful array elements. So, we go for queue based approach : 
Now, in queue, we keep only useful elements, and pop out all non useful elements.


## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).