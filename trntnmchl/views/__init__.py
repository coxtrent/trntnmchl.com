"""Views, one for each trntnmchl page."""
from trntnmchl.views.index import show_index
from trntnmchl.views.software import show_software
from trntnmchl.views.gallery import show_gallery
from trntnmchl.views.whoami import show_whoami
from trntnmchl.views.shop import show_shop
from trntnmchl.views.music import show_music
from trntnmchl.views.contact import show_contact
from trntnmchl.views.music_redirect import spotify, apple, soundcloud, youtube, bandcamp, new
from trntnmchl.before_request import before_request
from trntnmchl.views.live_audio import show_live_audio