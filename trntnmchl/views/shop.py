"""
trntnmchl shop view.

URLs include:
/
"""
from flask import render_template
import trntnmchl

@trntnmchl.app.route('/shop')
def show_shop():
    """Display /shop route."""
    context = {}
    return render_template("shop.html", **context)
