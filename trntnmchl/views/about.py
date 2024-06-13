"""
trntnmchl views.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/about')
def show_about():
    """Display trenton's graphic deisgn work."""
    context = {}
    return render_template("about.html", **context)

