
from collections import deque
def maximum_subarray(arr, k):
    result = []
    if len(arr) < k:
        return -1
    # Initializing deque
    Q = deque()
    # processing the first k elements
    for i in range(k):
        # keeping only the useful element
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k, len(arr)):

        result.append(arr[Q[0]])
        # sliding the window
        while Q and Q[0] <= i- k:
            Q.popleft()

        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()

        Q.append(i)




if __name__ == '__main__':
    maximum_subarray([12, 1, 78, 90, 57, 89, 56], 3) == [78, 90, 90, 90, 89]
    maximum_subarray([12, 1, 78], 3) == [78]
    maximum_subarray([12, 1], 3) == -1
    maximum_subarray([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
