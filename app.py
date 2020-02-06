from flask import Flask, render_template, redirect, request
import random
from redis import Redis
import os

domain = "http://127.0.0.1:5000/{}"

app = Flask(__name__)
app.config['REDIS_HOST'] = 'localhost'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0

db = Redis(app)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/', methods=['post'])
def get_short_url():
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        short_url = domain.format("".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',5)))# генерируем случайную последовательность из 5 символов для нашей короткой ссылки)
        db.set(short_url, long_url)
        return render_template('index.html', short_url = short_url) 

    return render_template('index.html')

@app.route('/<short_url>')
def redirect_short_url(short_url):
    long_url = db.get(short_url)
    return redirect(long_url)