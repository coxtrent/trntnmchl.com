"""Views, one for each trntnmchl page."""
from trntnmchl.views.index import show_index, show_cs, show_design
from trntnmchl.views.music_redirect import spotify, apple, soundcloud, youtube, bandcamp
from trntnmchl.views.https_redirect import before_request