from datetime import datetime, timedelta, date

users = [{'name': 'Євген Шевцов', 'birthday': '1991-08-11'},
         {'name': 'Дмитро Нестеренко', 'birthday': '1989-08-10'},
         {'name': 'Олексій Гамалій', 'birthday': '1970-08-07'},
         {'name': 'Андрій Мироненко', 'birthday': '1984-08-08'},
         {'name': 'Максим Шевченко', 'birthday': '1995-08-09'},
         {'name': 'Вікторія Талалай', 'birthday': '1998-06-30'},
         {'name': 'Дмитро Абрамов', 'birthday': '1981-06-19'},
         {'name': 'Дмитро Кратаєв', 'birthday': '1965-06-23'},
         {'name': 'Ірина Прус', 'birthday': '1990-08-23'},
         {'name': 'Вікторія Бойко', 'birthday': '1977-08-22'}]


def birth_reminder(users):
    current_year = date.today().year
    today = date.today()
    week_start = today - timedelta(days=today.weekday()-5)
    week_end = week_start + timedelta(days=6)
    result = {}
    # Пошук потрібних юзерів
    for user in users:
        user_birthday = datetime.strptime(user['birthday'], '%Y-%m-%d').date()
        age = current_year - user_birthday.year
        user_birthday = user_birthday.replace(year=current_year)
        if week_start <= user_birthday <= week_end:
            if user_birthday.weekday() < 5:
                result.setdefault(user_birthday.strftime(
                    '%A'), []).append([user['name'], age])
            else:
                result.setdefault('Monday', []).append([user['name'], age])

    return result


print(birth_reminder(users))
