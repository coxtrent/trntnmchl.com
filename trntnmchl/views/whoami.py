"""
trntnmchl views.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/whoami')
def show_whoami():
    """Display trenton's graphic deisgn work."""
    context = {}
    return render_template("whoami.html", **context)

