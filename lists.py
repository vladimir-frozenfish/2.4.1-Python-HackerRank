"""
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""

n = 1
spisok = [1,2, 10, 2]

for i in range(n):
    query_command = input().split()
    if query_command[0] == 'print':
        print(spisok)
    elif query_command[0] == 'append':
        spisok.append(int(query_command[1]))
    elif query_command[0] == 'insert':
        spisok.insert(int(query_command[1]), int(query_command[2]))
    elif query_command[0] == 'remove':
        spisok.remove(int(query_command[1]))
    elif query_command[0] == 'sort':
        spisok.sort()
    elif query_command[0] == 'pop':
        spisok.pop()
    elif query_command[0] == 'reverse':
        spisok.reverse()

