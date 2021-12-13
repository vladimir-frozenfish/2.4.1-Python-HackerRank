def wrap(string, max_width):
    count = 0
    s = ''
    while count < len(string):
        s += string[count:count+max_width] + '\n'
        count += max_width
    return s



print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 10))