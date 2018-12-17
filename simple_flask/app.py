from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Web site up and running"


@app.route('/<name>')
def foo(name):
    return "Foo {}!".format(name)


if __name__ == '__main__':
    app.run()
