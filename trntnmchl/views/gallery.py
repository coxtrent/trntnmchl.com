"""
trntnmchl graphic design examples.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/gallery')
def show_gallery():
    """Display sunboy gallery."""
    context = {}
    return render_template("gallery.html", **context)
