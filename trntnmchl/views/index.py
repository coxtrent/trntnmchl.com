"""
Insta485 index (main) view.

URLs include:
/
"""
import flask
import trntnmchl

@trntnmchl.app.before_request
def before_request():
    if not flask.request.is_secure:
        url = flask.request.url.replace('http://', 'https://', 1)
        code = 301
        return flask.redirect(url, code=code)

@trntnmchl.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)

@trntnmchl.app.route('/cs')
def show_cs():
    """Display trenton's CS portfolio."""
    context = {}
    return flask.render_template("cs.html", **context)


@trntnmchl.app.route('/design')
def show_design():
    """Display trenton's graphic deisgn work."""
    context = {}
    return flask.render_template("design.html", **context)


@trntnmchl.app.route('/about')
def show_about():
    """Display trenton's graphic deisgn work."""
    context = {}
    return flask.render_template("about.html", **context)

