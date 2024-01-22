from flask import Flask

from board import pages

def create_app():
    app = Flask(__name__)
    app.jinja_env.globals.update(zip=zip)
    app.register_blueprint(pages.bp)
    app.jinja_env.filters['zip'] = zip
    return app
 