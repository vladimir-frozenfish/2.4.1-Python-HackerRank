def solve(s):
    space = True
    full_name = ''
    for i in s:
        if i in [' ', '\t']:
            space = True
            full_name += i
        else:
            if space:
                full_name += i.upper()
                space = False
            else:
                full_name += i.lower()


    """
    s = s.split()
    full_name = ' '.join([i[0].upper() + i[1:].lower() for i in s])
    """

    """        
    full_name = (s[0].upper()
                 + s[1:space].lower()
                 + ' '
                 + s[space+1].upper()
                 + s[space+2:].lower())
    """
    print(full_name)


solve('vLaD kArpoVicH sdP 1 2fg')
solve(' hello   world    lol')