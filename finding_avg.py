student_marks = {'Вася': [10, 11, 23, 34, 3, 3, 7, 12],
                 'Петя': [5, 6, 2, 5, 6]}
query_name = 'Вася'
avg = sum(student_marks[query_name])/len(student_marks[query_name])

print(f'{avg:.2f}')