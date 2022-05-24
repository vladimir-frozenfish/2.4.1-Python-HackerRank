def itertools(A, B):
    for i in A:
        for j in B:
            print((i, j), end=' ')
    #print(A, B)


if __name__ == '__main__':
    a = (1, 2, 7)
    b = (3, 4, 9)

    itertools(a, b)