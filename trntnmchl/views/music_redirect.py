import flask
import trntnmchl

@trntnmchl.app.route('/spotify')
def spotify():
    return flask.redirect("https://open.spotify.com/artist/2J42S3cRKTqzz0upSLjsru", code=302)

@trntnmchl.app.route('/apple')
def apple():
    return flask.redirect("https://music.apple.com/us/artist/trenton-michael/1538264727", code=302)

@trntnmchl.app.route('/soundcloud')
def soundcloud():
    return flask.redirect("https://soundcloud.com/trentonmichael", code=302)

@trntnmchl.app.route('/bandcamp')
def bandcamp():
    return flask.redirect("https://trentonmichael.bandcamp.com/", code=302)

@trntnmchl.app.route('/youtube')
def youtube():
    return flask.redirect("https://www.youtube.com/channel/UCLimBHin2APkVTufIamLEOg", code=302)