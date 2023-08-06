from flask import Flask

from flask_geo import api


class FlaskGeo:

    def __init__(self, app: Flask = None, db):
        self.db = db
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.extensions['geo'] = self
        app.db = self.db
        api.init_app(app)
