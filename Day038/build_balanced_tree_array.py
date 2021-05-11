class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from collections import deque
# function for level order traversal for binary tree
def levelOrder(root):

    if not root:
        return

    queue = deque([])
    queue.append(root)

    while queue:

        temp = queue.popleft()
        print(temp.data, end = " ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

# main recursive function to build the balanced tree from array
def buildFromArray(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left =  buildFromArray(arr, start, mid - 1)
    root.right = buildFromArray(arr, mid + 1, end)

    return root

# driver test function
if __name__ == '__main__':
    arr, n = [1, 2, 3, 4, 5, 6, 7], 7
    root = buildFromArray(arr, 0, n - 1)
    levelOrder(root)
