from flask import Flask, request, render_template, url_for, redirect
from application import app
import requests
import random

@app.route('/',methods=['GET'])
def home():
        response = requests.get('http://localhost:5003/generatedname')
        print("hello!")
        generatedname = response.text
        return render_template('home.html',generatedname = generatedname, title = 'Home')