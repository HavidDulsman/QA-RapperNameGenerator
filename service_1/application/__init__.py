from flask import Flask, request
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

#MySQl Config
app.config['MYSQL_HOST'] = '35.246.123.192'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Duddybear12'
app.config['MYSQL_DB'] = 'rappernamegen'

from application import routes

    

