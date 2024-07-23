import datetime

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

day = 31
month = 8
year = 2019

day_of_week = get_day_of_week(day, month, year)

print(f"The day of the week for {day}/{month}/{year} is {day_of_week}")


