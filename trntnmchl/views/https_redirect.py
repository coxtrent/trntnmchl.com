from flask import Flask, request, redirect
import trntnmchl

@trntnmchl.app.before_request
def before_request():
    if request.url.startswith('http://') and not trntnmchl.app.debug:
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)

# Your routes here