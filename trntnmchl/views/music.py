"""
trntnmchl index view.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/music')
def show_music():
    """Display /music route."""
    context = {}
    return render_template("music.html", **context)
