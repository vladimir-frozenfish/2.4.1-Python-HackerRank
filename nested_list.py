students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

"""находим вторую по величине оценку"""
volume = set(i[1] for i in students)
volume.discard(min(volume))
volume = min(volume)

"""распечатываем имена с найденной оценкой"""
for i in students:
    if i[1] == volume:
        print(i[0])

print(' ')

"""распечатываем имена с найденной оценкой
в алфавитном порядке"""
students_second = []
for i in students:
    if i[1] == volume:
        students_second.append(i[0])

students_second.sort()
for i in students_second:
    print(i)


