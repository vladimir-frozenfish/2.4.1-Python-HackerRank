def minion_game(string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    STUART = 0
    KEVIN = 0
    len_string = len(string)

    for i in range(len_string):
        if string[i] in vowels:
            KEVIN += len_string - i
        else:
            STUART += len_string - i

    if STUART > KEVIN:
        return f'Stuart {STUART}'
    elif KEVIN > STUART:
        return f'Kevin {KEVIN}'
    return 'Draw'


print(minion_game('BANANA'))