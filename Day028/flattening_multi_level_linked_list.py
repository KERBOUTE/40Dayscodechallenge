class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.child = None

class LinkedList:

    def flatten(self, head):

        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr, tail = head, head

        while tail.next:
            tail = tail.next

        while ptr:

            if ptr.child:

                tail.next = ptr.child
                temp = ptr.child
                while temp.next:
                    temp =  temp.next
                tail = temp

            ptr = ptr.next


    def pretty_print(self, head):

        if not head:
            raise Exception ("Linked list is empty !!")
            return

        ptr = head
        while ptr != None:
            print(ptr.data, end = "->")
            ptr = ptr.next

# driver function
if __name__ == '__main__':

    head = Node(10)
    node1 = Node(5)
    node2 = Node(12)
    node3 = Node(7)
    node4 = Node(11)
    node5 = Node(4)
    node6 = Node(20)
    node7 = Node(13)
    node8 = Node(17)
    node9 = Node(6)
    node10 = Node(2)
    node11 = Node(16)
    node12 = Node(9)
    node13 = Node(8)
    node14 = Node(3)
    node15 = Node(19)
    node16 = Node(15)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head.child = node5
    node3.child = node8

    node5.next = node6
    node6.next = node7

    node8.next = node9

    node6.child = node10
    node7.child = node11
    node8.child = node12

    node12.next = node13

    node11.child = node14
    node12.child = node15

    node15.next = node16

    llist = LinkedList()
    llist.flatten(head)
    llist.pretty_print(head)
