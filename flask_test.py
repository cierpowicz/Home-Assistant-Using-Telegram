from flask import Flask

print("START")

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello, World!"
if __name__ == '__main__':
    app.run()
