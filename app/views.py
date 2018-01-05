#views.py

from flask import render_template,redirect,url_for
from app import app

@app.route('/')
def home():
	return render_template('home.html')
@app.route('/boyvgirl')
def boyvgirl():
	return render_template('GirlvsBoy.html')

@app.route('/mathvscience')
def mathvscience():
	return render_template('mathvscience.html')
@app.route('/intensefactors')
def intensefactors():
	return render_template('factorintense.html')
@app.route('/Factor')
def Factor():
	return render_template('Factors.html')