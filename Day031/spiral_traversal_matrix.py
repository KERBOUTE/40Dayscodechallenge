
def matrix_traversal(mat):
    m, n = len(mat), len(mat[0])
    if m == 0 and n == 0:
        return []

    k, l = 0, 0
    while k < m and l < n:
        for i in range(k, n, 1):
            print(mat[k][i], end = " ")
        k += 1

        for i in range(k, m, 1):
            print(mat[i][n - 1], end = " ")

        n -= 1
        if k < m:
            for i in range(n - 1, l - 1, -1):
                print(mat[m - 1][i], end = " ")
            m -= 1

        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(mat[i][l], end = " ")

            l += 1


# driver function
if __name__ == '__main__':
    mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

    # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix_traversal(mat)
