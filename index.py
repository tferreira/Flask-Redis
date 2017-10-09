from flask import Flask
from flask_redis import FlaskRedis
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = FlaskRedis(app)
