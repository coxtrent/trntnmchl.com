"""
trntnmchl computer science projects.

URLs include:
/
"""
from flask import render_template
import trntnmchl

def show_cs():
    """Display trenton's CS portfolio."""
    context = {}
    return render_template("cs.html", **context)