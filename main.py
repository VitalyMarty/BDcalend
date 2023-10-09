from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(days=7)

    if not users or all(user['birthday'] < today for user in users):
        return {}

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthday_dict = {day: [] for day in days_of_week}

    for user in users:
        name = user['name']
        birthday = user['birthday']

        if today <= birthday < next_week:
            day_of_week = birthday.strftime('%A')

            if day_of_week not in ['Saturday', 'Sunday']:
                birthday_dict[day_of_week].append(name)

                current_year = today.year
                current_date = today.replace(year=current_year)
                if birthday.month == 1:
                    birthday_this_year = birthday.replace(year=current_year + 1)
                else:
                    birthday_this_year = birthday.replace(year=current_year)

                if birthday_this_year < current_date:
                        continue


    return birthday_dict

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        if names:
            print(f"{day_name}: {', '.join(names)}")
        else:
            print(f"{day_name}: No birthdays")
