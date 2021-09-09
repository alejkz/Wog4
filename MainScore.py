from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    STATIC_SCORE = 7
    STATIC_ERROR = 403

    try:
        return "Hello! Score is <div id="score">{STATIC_SCORE}</div>"

    except TypeError:
        return "<h1><div id="score" style="color:red">{STATIC_ERROR}</div></h1>"


if __name__ == "__main__":
    app.run()