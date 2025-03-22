from flask import Flask
import random

app = Flask(__name__)
lucky_number = 0


@app.route('/')
def guess_number():
    global lucky_number
    lucky_number = random.randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route('/<number>')
def check_number(number):
    if int(number) < lucky_number:
        return "<h1>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    elif int(number) > lucky_number:
        return "<h1>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    else:
        return "<h1>You found me!!!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run()
