"""
подсчет максиму песочных часов
123
 4
565
в матрице 6*6
"""

def hourglassSum(arr):
    sand_watch = []

    for i in range(4):
        for j in range(4):
            sand_watch.append(sum(arr[i][j:j+3])
                          + arr[i+1][j+1]
                          + sum(arr[i+2][j:j+3]))

    return max(sand_watch)

arr = [
    [0, -4, -6, 0, -7, -6],
    [-1, -2, -6, -8, -3, -1],
    [-8, -4, -2, -8, -8, -6],
    [-3, -1, -2, -5, -7, -4],
    [-3, -5, -3, -6, -6, -6],
    [-3, -6, 0, -8, -6, -7]
]

print(hourglassSum(arr))