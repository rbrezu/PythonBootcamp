import calendar

cal = calendar.Calendar(3)

year = int(input('Year: '))
month = int(input('Month(1 - 12): '))

text_cal = calendar.TextCalendar(3).formatmonth(year, month, 4)
text_cal = text_cal.replace(' 16', '*16')
text_cal = text_cal.replace(' 21', '*21')
print(text_cal)
