import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']

mysql = MySQL(app)

url = "http://34.89.30.20/"

def test_url_service1():
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    assert 200 == r.status
