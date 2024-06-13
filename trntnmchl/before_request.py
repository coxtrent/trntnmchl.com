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
    url = None
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
    if request.url.startswith('https://www.'):
        url = request.url.replace('https://www.', 'https://', 1)
        code = 301

    if url is not None:
        return redirect(url, code=code)
