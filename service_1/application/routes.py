from flask import Flask, request, render_template, url_for, redirect
from application import app
from flask_mysqldb import MySQL
import requests
import random

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
                response = requests.get('http://end_product:5003/generated3')
                generatedname = response.text
                print(generatedname)
                details = request.form
                username = details['username']
                print(username)
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO entries(name_old, name_new) VALUES (%s, %s)", (username,generatedname))
                mysql.connection.commit()
                cur.close()
                return render_template('home.html',generatedname = generatedname, title = 'Home')
        else:
                return render_template("index.html")

@app.route('/home',methods=['GET'])
def home():
        if request.method == 'POST':
                response = requests.get('http://end_product:5003/generated3')
                generatedname = response.text
                print(generatedname)
                details = request.form
                username = details['username']
                print(username)
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO entries(name_old, name_new) VALUES (%s, %s)", (username,generatedname))
                mysql.connection.commit()
                cur.close()
        return render_template('home.html',generatedname = generatedname, title = 'Home')

