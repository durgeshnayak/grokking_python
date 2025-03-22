import smtplib
import datetime
import random

quotes = []
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

DAY_OF_THE_WEEK = "Monday"


def load_quotes():
    global quotes
    try:
        with open(file="./quotes.txt", mode="r") as file_stream:
            quotes = file_stream.readlines()
    except FileNotFoundError:
        print("The file quotes.txt was not found")
    else:
        return quotes


def get_random_quote():
    global quotes
    if len(quotes) > 0:
        return random.choice(quotes)
    else:
        return "Insanity is doing the same thing over and over and expecting a different outcome. - Einstein"


def create_email(quote):
    email_content = f"Subject:Monday Motivational Quotes\n\n{quote}"
    return email_content


def send_email(email_content):
    my_email = "pythonjunkie25@gmail.com"
    password = "rsfxkrxhzzdunzlk"

    connection = smtplib.SMTP(host="smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="pythonjunkie25@yahoo.com",
                        msg=email_content)
    connection.close()


load_quotes()
now = datetime.datetime.now()
day_of_the_week = days_of_the_week[now.weekday()]

if day_of_the_week == DAY_OF_THE_WEEK:
    send_email(create_email(get_random_quote()))
