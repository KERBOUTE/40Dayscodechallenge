
def ternary_search(arr, key):

    start, end = 0, len(arr) - 1

    while start <= end:
        mid1 = start + (end  - start) // 3
        mid2 = end - (end  - start) // 3
        print(mid1)
        print(mid2)
        if key == arr[mid1]:
            return mid1

        if key == arr[mid2]:
            return mid2

        if key < arr[mid1]:
            end = mid1 - 1
        elif key > arr[mid2]:
            start = mid2 + 1
        else:
            start = mid1 + 1
            end = mid2 - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"ans : {ternary_search(arr, 10)}")
