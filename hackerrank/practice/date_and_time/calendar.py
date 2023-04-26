# Date and Time - calendar
import calendar

month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday]
print(weekday_name.upper())
