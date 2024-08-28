#!/usr/bin/env python3
"""
setup a basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    instiantiated config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def hello_world():
    """
    method 2 return hello world
    """
    return render_template("1-index.html")

@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run(debug=True)
