"""
trntnmchl views.

URLs include:
/
"""
from flask import request, redirect
import trntnmchl

@trntnmchl.app.before_request
def before_request():
    """Redirect to HTTPS and remove www."""
    print("\n\n\nbefore_request called\n\n\n")
    url = None
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
    if 'www.' in request.url:
        url = request.url.replace('www.', '', 1)

    if url is not None:
        return redirect(url, code=301)
