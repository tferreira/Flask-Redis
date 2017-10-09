from flask import Flask
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
