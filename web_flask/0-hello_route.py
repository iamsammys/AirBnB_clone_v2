#!/usr/bin/python3
"""Script to start a flask web application
"""

from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Prints a string in a web browser

    Return:
        string
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    subprocess.run("export, FLASK_APP=0-hello_route.py")
    subprocess.run("flask run")
