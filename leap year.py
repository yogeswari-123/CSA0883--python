import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

date_str = input("Enter Date (MM/DD/YYYY): ")
date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
year = date_obj.year

if is_leap_year(year):
    next_date = date_obj.replace(year=year + 1)
    print(f"Given Anniversary Year: Leap Year.")
    print(f"Anniversary Date: {next_date.strftime('%m/%d/%Y')}")
else:
    prev_date = date_obj.replace(year=year - 1)
    print(f"Given Anniversary Year: Non Leap Year.")
    print(f"Anniversary Date: {prev_date.strftime('%m/%d/%Y')}")
