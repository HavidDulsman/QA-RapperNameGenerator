from flask import Flask, request, render_template, url_for, redirect
from flask_mysqldb import MySQL
from application import app
import requests
import random

#MySQl Config
app.config['MYSQL_HOST'] = '35.246.123.192'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Duddybear12'
app.config['MYSQL_DB'] = 'rappernamegen'

@app.route('/',methods=['GET'])
def home():
        response = requests.get('http://localhost:5003/generated3')
        print("hello!")
        generatedname = response.text
        print(generatedname)
        return render_template('home.html',generatedname = generatedname, title = 'Home')

