#!/usr/bin/env python3
"""
setup a basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@app.route("/")
def hello_world():
    """
    method 2 return hello world
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
