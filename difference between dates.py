from datetime import datetime

date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")


difference = abs((date2 - date1).days)
print(f"The difference between {date1_str} and {date2_str} is {difference} days")
