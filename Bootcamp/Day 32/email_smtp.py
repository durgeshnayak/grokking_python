import smtplib

my_email = "pythonjunkie25@gmail.com"
password = "rsfxkrxhzzdunzlk"

connection = smtplib.SMTP(host="smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="pythonjunkie25@yahoo.com",
                    msg="Subject:Hello Junkie\n\nThis email was sent from python code.")
connection.close()
