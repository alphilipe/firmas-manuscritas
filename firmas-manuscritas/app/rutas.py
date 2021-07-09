from app import app
from flask import Flask, render_template

from app.static.firmas.modelo import modelo_h5

#import keras
#from keras.models import load_model


model=modelo_h5('./static/modelos/firmas_manuscritas_07_07.h5')

@app.route('/')
@app.route('/home')
def home():
    return "BienBenido a home"

@app.route('/index/')
def index():

    return render_template('index.html', mi_pie= modelo_h5('./static\modelos/firmas_manuscritas_07_07.h5'))