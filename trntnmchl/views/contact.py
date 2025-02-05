"""
trntnmchl contact page view.

URLs include:
/contact
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/contact')
def show_contact():
    """Display /contact route."""
    context = {}
    return render_template("contact.html", **context)
