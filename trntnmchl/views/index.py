"""
Insta485 index (main) view.

URLs include:
/
"""
import flask
import os
from flask_talisman import Talisman
import trntnmchl

if 'DYNO' in os.environ:  # only trigger Talisman if the app is running on Heroku
    Talisman(trntnmchl.app)

@trntnmchl.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)

@trntnmchl.app.route('/cs')
def show_cs():
    """Display trenton's CS portfolio."""
    context = {}
    return flask.render_template("cs.html", **context)


@trntnmchl.app.route('/design')
def show_design():
    """Display trenton's graphic deisgn work."""
    context = {}
    return flask.render_template("design.html", **context)


@trntnmchl.app.route('/about')
def show_about():
    """Display trenton's graphic deisgn work."""
    context = {}
    return flask.render_template("about.html", **context)

