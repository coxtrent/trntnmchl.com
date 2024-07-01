"""Views, one for each trntnmchl page."""
from trntnmchl.views.index import show_index
from trntnmchl.views.software import show_software
from trntnmchl.views.gallery import show_gallery
from trntnmchl.views.whoami import show_whoami
from trntnmchl.views.shop import show_shop
from trntnmchl.views.music import show_music
from trntnmchl.views.music_redirect import spotify, apple, soundcloud, youtube, bandcamp
from trntnmchl.before_request import before_request