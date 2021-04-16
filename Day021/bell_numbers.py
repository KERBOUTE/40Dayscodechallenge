
def compute_bell_number(n):
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n - 1][0]

if __name__ == '__main__':
    print(compute_bell_number(10))
