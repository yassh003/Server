from flask import Flask
app = Flask(__name__)

@app.route('/')
def server():
    return "Server is up and running"

if __name__ == '__main__':
    app.debug = True
    app.run()