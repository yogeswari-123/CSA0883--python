def get_season(month, day):
    
    seasons = {
        "Mar": (20, "Summer"),
        "Jun": (21, "Spring"),
        "Sep": (22, "Fall"),
        "Dec": (21, "Winter")
    }

    
    month = month[:3].capitalize()

    if month in ["Jan", "Feb"] or (month == "Mar" and day < 20):
        return "Winter"
    elif (month == "Mar" and day >= 20) or month in ["Apr", "May"] or (month == "Jun" and day < 21):
        return "Summer"
    elif (month == "Jun" and day >= 21) or month in ["Jul", "Aug"] or (month == "Sep" and day < 22):
        return "Spring"
    elif (month == "Sep" and day >= 22) or month in ["Oct", "Nov"] or (month == "Dec" and day < 21):
        return "Fall"
    else:
        return "Winter"


month = input("Enter the month (first three letters with first letter capital): ")
day = int(input("Enter the date: "))

season = get_season(month, day)
print(f"The season is currently {season}")

