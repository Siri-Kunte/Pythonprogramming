#program to calculate nuber of seconds in a day/week/month

#finding the number of secodns in a day
seconds_day = 60* 60* 24
print(seconds_day)

#finding the number of seconds in a week
seconds_week = seconds_day * 7
print(seconds_week)

#finding the number of seconds in a month
seconds_month = seconds_day * 30
print(seconds_month)

#finding the number of seconds in a year
seconds_year = seconds_day * 365
print(seconds_year)

#Using conditionals
marks = int(input("Enter the marks of Student:"))
print(type(marks))

if marks >= 18:
    print("The Student has passed the exam")
else:
    print("The Student has failed the exam")





