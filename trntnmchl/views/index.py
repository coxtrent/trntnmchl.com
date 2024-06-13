"""
trntnmchl index view.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return render_template("index.html", **context)
