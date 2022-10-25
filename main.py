from flask import Flask, render_template
from writing import Writing
from datetime import datetime

app = Flask(__name__)
writing = Writing()


@app.route('/')
def home():
    return render_template("index.html", writing=writing.writing, year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
