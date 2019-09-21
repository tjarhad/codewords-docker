from flask import Flask
from os import environ

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def first_app():
    with open('logs/log.txt', 'a') as log_file:
        log_file.write('Hello File\n')
    return f"Hello World this is {environ.get('NAME')}"


if __name__ == '__main__':
    app.run("0.0.0.0", port="5000")
