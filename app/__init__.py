# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    db.app = app

    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(app.main_blueprint)
    # 附加路由和自定义的错误页面

    return app
