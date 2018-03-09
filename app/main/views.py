from flask import render_template

from app import db
from app.models.user import User

from . import main


@main.route('/')
def index():
    # return render_template('main/index.html')
    user = User()
    s = user.get_one('xuwuqiang')
    print(s)
    print(s.name)

    u = User()
    u.email = 'test'
    u.name = 'pytest'
    db.session.add(u)
    return "index"


@main.route('/about')
def about():
    return "about"
