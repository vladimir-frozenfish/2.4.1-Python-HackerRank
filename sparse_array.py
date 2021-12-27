def matchingStrings(strings, queries):
    return [strings.count(i) for i in queries]

strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
print(matchingStrings(strings, queries))