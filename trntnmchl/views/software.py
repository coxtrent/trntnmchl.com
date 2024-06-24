"""
trntnmchl computer science projects.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/software')
def show_software():
    """Display trenton's CS portfolio."""
    context = {}
    return render_template("software.html", **context)