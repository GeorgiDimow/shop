import os

import cloudinary
import cloudinary.uploader
import cloudinary.api


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Goshoprasetolosho123!@localhost/wood_shop_schema'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['ined_et@abv.bg']

    cloudinary.config(
        cloud_name="dvozlwvz0",
        api_key="511373944373463",
        api_secret="eBbW2CxXu24yv3s6ArJu6qhPaQY",
        secure=True
    )