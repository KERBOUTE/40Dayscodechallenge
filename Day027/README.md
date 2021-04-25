# Circular_linked_lists
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 027, is a problem recently posed by Amazon:


Program for constructing and maintaining circular linked lists
complexity asymtodic bounds are pretty much similar to what we have seen in single linked list/double linked lists


```
#structure node class

class Node:

#class for circular_linked_lists

class circular_linked_lists:

    def __init__(self):
        self.head = None

    # function for inserting the node after the list (end of list)
    def push(self, x):

        
    # printing the traversal of circular_linked_lists
    # now here, the things are little tricky as we have to keep a note of starting point of traversal,
    # wherein single/double linked lists, we always have convention to start from head and then traverse till last,
    # in circular_linked_lists, we can start from any node (including head), and can traverse the entire list as the list is circular.

    def pretty_print(self, starting_point):
        # base case when linked list is empty
         
        

        # initialising the ptr (temporary pointer) to head


        # firstly we move to starting point and then stop there


        # now we start traversing from starting point (considering it as head)

# driver function
if __name__ == '__main__':

    cllist = circular_linked_lists()
    cllist.push(0)
    cllist.push(1)
    cllist.push(2)
    cllist.push(3)
    cllist.pretty_print(2)  # 2->3->0->1
    # printing from different starting points can have different representations
```

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).