import re
import datetime

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
password_regex = r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'

email = input("Введите email: ")
password = input("Введите пароль: ")

if not re.match(email_regex, email):
    print("Email введен неправильно")
    exit()

if not re.match(password_regex, password):
    print("Пароль введен неправильно")
    exit()

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M:%S")

with open('data.txt', 'a') as f:
    f.write(f'{email} {password} {date}\n')