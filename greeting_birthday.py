from datetime import datetime, timedelta

users = [{'name':'Bill', 'birthday':'21/01/1970'}, {'name':'Mark', 'birthday':'22/02/1970'}, {'name':'Fil', 'birthday':'23/03/1987'},
{'name':'Mike', 'birthday':'29/06/1990'}, {'name':'Alice', 'birthday':'30/07/1991'}, {'name':'Greg', 'birthday':'01/08/1974'},
{'name':'Tom', 'birthday':'05/08/1981'}, {'name':'Jeny', 'birthday':'31/07/1995'}, {'name':'Rupert', 'birthday':'03/08/1971'},
{'name':'Bill', 'birthday':'04/08/1992'}, {'name':'Jim', 'birthday':'08/12/1962'}, {'name':'Saymon', 'birthday':'03/08/1982'}]

def get_birthdays_per_week(users: list) -> None:

    day_of_weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    current_date = datetime.now()

    if current_date.weekday() == 5:
        begin_day_of_next_week = current_date
    elif current_date.weekday() == 6:
        begin_day_of_next_week = current_date - timedelta(days=1)
    else:
        while current_date.weekday() != 5:
            current_date += timedelta(days=1) 
            begin_day_of_next_week = current_date

    days_of_next_week = []
    for day in range(7):
        days_of_next_week.append(begin_day_of_next_week + timedelta(days=day))

    users_birthday_next_week = {}
    for user in users:
        name = user['name']
        birthday = datetime.strptime(user['birthday'], '%d/%m/%Y')
        for day in days_of_next_week:
            if birthday.month == day.month and birthday.day == day.day:
                users_birthday_next_week[name] = day

    birthdays_by_day = {}
    for name, birthday in users_birthday_next_week.items():
        if birthday.weekday() == 5 or birthday.weekday() == 6:
            day_index = 0
        else:
            day_index = birthday.weekday()
        day_of_week = day_of_weeks[day_index]
        if day_of_week in birthdays_by_day:
            birthdays_by_day[day_of_week].append(name)
        else:
            birthdays_by_day[day_of_week] = [name]

    for day, names in birthdays_by_day.items():
        names_str = ", ".join(names)
        print(f"{day}: {names_str}")

    return


# get_birthdays_per_week(users)


if __name__ == "__main__":
    get_birthdays_per_week(users)