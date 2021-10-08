from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.DATABASE_USER}:' \
                                        f'{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}:' \
                                        f'{config.DATABASE_PORT}/{config.DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

