def sum_array(l1, l2, m, n):

    i = m - 1
    j = n - 1
    carry = 0
    ans = []

    while(j >= 0):
        temp = l1[i] + l2[j] + carry
        ans.append(temp%10)
        carry = temp // 10

        j -= 1
        i -= 1

    while(i >= 0):
        temp = l1[i] + carry
        ans.append(temp%10)
        carry = temp // 10
        i -= 1

    if (carry):
        ans.append(carry)
    return ans[::-1]

def sum_main(l1, l2, m, n):
    if m >= n:
        return sum_array(l1, l2, m, n)
    else:
        return sum_array(l2, l1, n, m)

if __name__ == '__main__':
    m = int(input().strip())
    l1 = list(map(int, input().strip().split()))
    n = int(input().strip())
    l2 = list(map(int, input().strip().split()))
    s = sum_main(l1, l2, m, n)
    for i in range(len(s)):
        s[i] = str(s[i])
    print(' '.join(s))

'''
assert sum_main([1, 2, 3, 4, 5, 6], [6, 7, 8, 9], 6, 4) == [1, 3, 0, 2, 4, 5]
'''
