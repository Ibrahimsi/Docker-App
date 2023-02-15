from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """This is my 1st Project
                I used ChatGPT for this python program
                And Deploy the application in the Docker container"""

if __name__ == "__main__":
    app.run(host='0.0.0.0')

