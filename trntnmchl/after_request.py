from flask import Flask
import trntnmchl

app = Flask(__name__)

def setup_after_request(app):
    @app.after_request
    def set_frame_options(response):
        """Set Content-Security-Policy for iframe control."""
        # Adjust the domain below to your site's domain
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https://sunboyforever.com;"
        return response