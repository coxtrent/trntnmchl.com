"""Views, one for each trntnmchl page."""
from trntnmchl.views.index import show_index
from trntnmchl.views.cs import show_cs
from trntnmchl.views.design import show_design
from trntnmchl.views.about import show_about
from trntnmchl.views.shop import show_shop
from trntnmchl.views.music_redirect import spotify, apple, soundcloud, youtube, bandcamp
from trntnmchl.before_request import before_request