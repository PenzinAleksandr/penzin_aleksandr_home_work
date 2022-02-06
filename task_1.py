seconds = int(input('Введите продолжительность: '))

duration = seconds

new_seconds = duration % 60
new_minutes = duration // 60 % 60
new_hours = duration // 3600 % 24
new_days = duration // 3600 // 24


if duration < 60:
    print(new_seconds, 'сек')
elif duration >= 60 and duration < 3600:
    print(new_minutes, 'мин', new_seconds, 'сек')
elif duration >= 3600 and duration < 86400:
    print(new_hours, 'час', new_minutes, 'мин', new_seconds, 'сек')
else:
     print(new_days, 'дн', new_hours, 'час', new_minutes, 'мин', new_seconds, 'сек')
