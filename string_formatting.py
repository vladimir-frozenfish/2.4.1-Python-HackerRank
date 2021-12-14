"""
функция выводит от 1 до number:
Десятичное, Восмеричное, 16-ричное, Двоичное
"""
def print_formatted(number):
    space = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        i_10 = str(i)
        i_8 = str(oct(i)[2:])
        i_16 = str(hex(i)[2:]).upper()
        i_2 = str(bin(i)[2:])
        print(i_10.rjust(space), i_8.rjust(space), i_16.rjust(space), i_2.rjust(space))

print_formatted(100)
