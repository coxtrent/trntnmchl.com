"""Views, one for each trntnmchl page."""
from trntnmchl.views.index import show_index, show_cs, show_design, before_request, show_about
from trntnmchl.views.music_redirect import spotify, apple, soundcloud, youtube, bandcamp