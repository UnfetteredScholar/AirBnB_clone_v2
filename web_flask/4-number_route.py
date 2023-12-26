#!/usr/bin/python3
"""
Defines a Flask web app with routes
"""
from flask import Flask

app = Flask(__name__)


@app.get("/", strict_slashes=False)
def index():
    """
    Root endpoint of Flask application

    Returns:
        (str) Hello HBNB!
    """
    return "Hello HBNB!"


@app.get("/hbnb", strict_slashes=False)
def get_hbnb():
    """
    hbnb endpoint of Flask application

    Returns:
        HBNB
    """
    return "HBNB"


@app.get("/c/<text>", strict_slashes=False)
def get_c(text):
    """
    Returns C followed by the path parameter
    """
    return f"C {text}".replace("_", " ")


@app.get("/python/", defaults={"text": "is cool"})
@app.get("/python/<text>", strict_slashes=False)
def get_python(text):
    """
    Returns Python followed by the path parameter
    """
    return f"Python {text}".replace("_", " ")


@app.get("/number/<int:n>")
def get_number(n):
    """
    Returns 'n is a number if the route param is an int
    """

    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
