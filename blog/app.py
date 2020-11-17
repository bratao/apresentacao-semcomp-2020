# -*- coding: utf-8 -*-
from diskcache import Cache
from flask import Flask, render_template, request, flash, Markup, jsonify

from flask_wtf import  CSRFProtect

from flask_bootstrap import Bootstrap

import db

app = Flask(__name__)
app.secret_key = 'dev'


# set default button sytle and size, will be overwritten by macro parameters
app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'
# app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'  # uncomment this line to test bootswatch theme

bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():

    recent_news = db.News.select().order_by(
        db.News.date_published.desc()).limit(10)

    return render_template('index.html', noticias=recent_news)


@app.before_first_request
def before_first_request_func():
    pass


if __name__ == '__main__':
    app.run(debug=True)
