from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/durgesh')
def hello_durgesh():
    return 'Hello, Durgesh!'


if __name__ == "__main__":
    app.run()

    