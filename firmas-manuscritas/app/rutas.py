from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/home')
def home():
    return "BienBenido a home"

@app.route('/index/')
def index():
    return render_template('index.html')