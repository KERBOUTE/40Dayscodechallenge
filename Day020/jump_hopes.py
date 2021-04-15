
def canReachEnd(arr):
    n = len(arr)
    for i in range(n):
        ptr = i
        print(f"outer ptr : {ptr}")
        while ptr < n and arr[ptr] != 0:
            print(f"inner ptr : {ptr}")
            if ptr == n - 1:
                return 1
            if arr[ptr] == 0:
                return 0
            ptr = ptr + arr[ptr]
            print("inner finished ")


if __name__ == '__main__':
    arr = [3, 2, 1, 0, 4]
    print(canReachEnd(arr))
