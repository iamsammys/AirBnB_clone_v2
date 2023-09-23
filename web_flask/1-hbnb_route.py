#!/usr/bin/python3
"""Python script to start a web app
"""

from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function to display a string in a web browser using flask web app

    Return:
        string
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Displays a string 'HBNB' in a web browser

    Return:
        string
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
