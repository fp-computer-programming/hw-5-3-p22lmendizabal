# author: LM (AMDG) 10/29/21
import calendar
# Question 1
calendar.TextCalendar().pryear(2020)
# Question 2
calendar.setfirstweekday(6)
print(calendar.calendar(2020))
# Question 3
print(calendar.month(2021, 8))
# Question 4
calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)
calendar.LocaleTextCalendar(6, "KOREAN").pryear(2020)
calendar.LocaleTextCalendar(6, "DUTCH").pryear(2020)
#calendar.LocaleTextCalendar(6, "MANDARIN").pryear(2020)
# Question 5
print(calendar.isleap(2020))
# it is a boolean. Returns either true or false
