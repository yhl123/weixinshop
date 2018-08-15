from flask import Flask
from .views.weixin_index import weixin_index


def create_app():
    app=Flask(__name__,template_folder='templates',static_folder='static')
    app.config.from_object('settings.DevelopmentConfig')
    app.register_blueprint(weixin_index)
    return app