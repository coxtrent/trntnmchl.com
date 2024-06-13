"""
trntnmchl graphic design examples.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/design')
def show_design():
    """Display trenton's graphic deisgn work."""
    context = {}
    return render_template("design.html", **context)
