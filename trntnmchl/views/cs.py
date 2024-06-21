"""
trntnmchl computer science projects.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/cs')
def show_cs():
    """Display trenton's CS portfolio."""
    context = {}
    return render_template("cs.html", **context)