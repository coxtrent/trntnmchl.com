"""
trntnmchl views.

URLs include:
/
"""
from flask import request, redirect
import trntnmchl

@trntnmchl.app.before_request
def before_request():
    """Remove the www."""
    if 'www.' in request.url:
        url = request.url.replace('www.', '', 1)
        return redirect(url, code=301)
