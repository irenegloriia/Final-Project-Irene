from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import json
from gabung import gabung

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from flask_socketio import send, emit

@app.route('/')
def home():
	return render_template('berita.html') 

@socketio.on('my event')
def handle_my_custom_event(json):
    print(json['data'])
    item = gabung(json['data'])
    print(item)
    emit('my response', item)
    

if __name__ == '__main__':
    socketio.run(app)