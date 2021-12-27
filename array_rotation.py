def rotateLeft(d, arr):
    rotate = d % len(arr)
    rotate_array = arr[rotate:] + arr[:rotate]
    return rotate_array

print(rotateLeft(54, [1, 2, 3, 4, 5]))