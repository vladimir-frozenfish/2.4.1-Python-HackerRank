import calendar

'''
print(calendar.TextCalendar(firstweekday=7).formatyear(2022))
print(calendar.weekday(2022, 4, 8))
print(calendar.weekheader(10))
'''

MM, DD, YYYY = list(map(int, input().split()))

day_week = {
    0: 'MONDAY',
    1: 'TUESDAY',
    2: 'WEDNESDAY',
    3: 'THURSDAY',
    4: 'FRIDAY',
    5: 'SATURDAY',
    6: 'SUNDAY',
}

print(day_week[calendar.weekday(YYYY, MM, DD)])

