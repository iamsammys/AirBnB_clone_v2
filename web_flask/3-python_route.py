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


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Displays 'C' with the text passed as variable to the url and replaces _
    with space

    Returns:
        string
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    """Displays “Python ”, followed by the value of the text variable

    Returns:
        string
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
