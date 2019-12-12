import requests
from requests_oauthlib import OAuth1Session

from os import environ


class Flickr():
    def __init__(self):
        self.base_string = "https://www.flickr.com/services/oauth/request_token?oauth_nonce=89601180&oauth_timestamp=1305583298&oauth_consumer_key=" + environ.get(
            'FLICKR_KEY') + "&oauth_signature_method=HMAC-SHA1&oauth_version=1.0&oauth_callback=http%3A%2F%2Fwww.example.com"

        self.get_request_token()

    def get_request_token(self):
        base_string = "GET&https%3A%2F%2Fwww.flickr.com%2Fservices%2Foauth%2Frequest_token&oauth_callback%3Dhttp%253A%252F%252Flvh.me%26oauth_consumer_key%3D9ee326d37fb547a145636fb08eb20c82%26oauth_nonce%3D95613465%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1305586162%26oauth_version%3D1.0"

        consumer_key = environ.get('FLICKR_KEY')
        hmac_key = consumer_key + '&' + environ.get('FLICKR_SECRET')
        print(hmac_key)
        oauth = OAuth1Session(environ.get('FLICKR_KEY'), client_secret=hmac_key, callback_uri='lvh.me', signature_method='HMAC-SHA1')
        response = oauth.fetch_request_token('https://www.flickr.com/services/oauth/request_token')
        print(response)
