from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'
    return 'This is my first cicd project'

if __name__ == '__main__':
    app.run()


