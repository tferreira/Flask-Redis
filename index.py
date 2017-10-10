from flask import Flask
from flask_redis import FlaskRedis
from redis import StrictRedis
from config import BaseConfig


class DecodedRedis(StrictRedis):
    @classmethod
    def from_url(cls, url, db=None, **kwargs):
        kwargs['decode_responses'] = True
        return StrictRedis.from_url(url, db, **kwargs)


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = FlaskRedis.from_custom_provider(DecodedRedis, app)

