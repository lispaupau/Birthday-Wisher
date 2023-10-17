import smtplib
import datetime as dt
import pandas
import random

my_email = 'enter_your_mail'
password = 'enter_your_password'

data = pandas.read_csv('birthdays.csv')

now = dt.datetime.now()
day = now.day
month = now.month

its_birthday = data[(data['day'] == day) & (data['month'] == month)].to_dict(orient='records')

letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

with open(random.choice(letters), 'r') as f:
    new_letter = f.read()
    name = its_birthday[0]['name']
    if '[NAME],' in new_letter.split():
        new_letter = new_letter.replace('[NAME],', f'{name},')

with smtplib.SMTP('smtp.inbox.ru') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=its_birthday[0]['email'],
                        msg=f'Subject:Happy Birthday\n\n{new_letter}')

