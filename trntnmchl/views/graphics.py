"""
trntnmchl graphic design examples.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/graphics')
def show_graphics():
    """Display trenton's graphic deisgn work."""
    context = {}
    return render_template("graphics.html", **context)
