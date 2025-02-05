"""
trntnmchl index view.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/live_audio')
def show_live_audio():
    """Display /live_audio route."""
    context = {}
    return render_template("live_audio.html", **context)
